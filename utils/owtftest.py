import os
import re
import sys
import subprocess

import unittest
import mock
from hamcrest import *

from utils.clean import db_setup, clean_owtf_review
from utils.service.web.server import WebServerProcess, HandlerBuilder

import owtf


class OWTFTestCase(unittest.TestCase):

    """Basic OWTF test case that initialises basic patches."""

    PROTOCOL = 'http'
    IP = '127.0.0.1'
    PORT = '8888'

    def setUp(self):
        self.clean_old_runs()
        self.raw_input_patcher = mock.patch('__builtin__.raw_input', return_value=['Y'])
        self.log_info_patcher = mock.patch('owtf.logging.info')
        self.log_warn_patcher = mock.patch('owtf.logging.warn')
        self.raw_input_patcher.start()
        self.mock_log_info = self.log_info_patcher.start()
        self.mock_log_warn = self.log_warn_patcher.start()

    def tearDown(self):
        self.raw_input_patcher.stop()
        self.log_info_patcher.stop()
        self.log_warn_patcher.stop()

    @staticmethod
    def clean_old_runs():
        """Clean the database and the older owtf_review directory."""
        # Reset the database.
        db_setup('clean')
        db_setup('init')
        # Remove old OWTF outputs
        clean_owtf_review()


class OWTFCliTestCase(OWTFTestCase):

    """OWTF test case for testing the CLI."""

    DEFAULT_ARGS = ['owtf.py', '--nowebui']

    def __init__(self, methodName='runTest'):
        super(OWTFCliTestCase, self).__init__(methodName)
        self.args = self.DEFAULT_ARGS

    def setUp(self):
        super(OWTFCliTestCase, self).setUp()
        self.args = self.DEFAULT_ARGS

    @classmethod
    def run_owtf(cls, args=None):
        """Run OWTF with args."""
        args = args or cls.DEFAULT_ARGS
        owtf.main(args)

    @staticmethod
    def assert_called_with(mock_obj, *args):
        """Assert that ``mock_obj`` has been called with all elements from
        ``args`` (in order).
        """
        mock_obj.assert_any_call(*args)


class OWTFWebPluginTestCase(unittest.TestCase):

    PROTOCOL = 'http'
    IP = '127.0.0.1'
    PORT = '8888'
    MATCH_PLUGIN_START = 'Execution Start'
    MATCH_BUG = 'OWTF BUG'
    DYNAMIC_METHOD_REGEX = "^set_(head|get|post|put|delete|options|connect)_response"

    def setUp(self):
        # Reset the database.
        db_setup('clean')
        db_setup('init')
        self.raw_input_patcher = mock.patch('__builtin__.raw_input', return_value=['Y'])
        self.interface_server_patcher = mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
        self.run_plugin_patcher = mock.patch('framework.plugin.plugin_handler.PluginHandler.RunPlugin', return_value='')
        self.rank_plugin_patcher = mock.patch('framework.plugin.plugin_handler.PluginHandler.rank_plugin', return_value='-1')
        self.raw_input_patcher.start()
        self.mock_run_plugin = self.run_plugin_patcher.start()
        self.mock_rank_plugin = self.rank_plugin_patcher.start()
        # Web server initialization.
        self.responses = {}
        self.server = WebServerProcess(self.IP, self.PORT, self.build_handlers())
        self.server.start()

    def tearDown(self):
        self.raw_input_patcher.stop()
        self.run_plugin_patcher.stop()
        self.rank_plugin_patcher.stop()
        self.server.stop()
        # Reset the database.
        db_setup('clean')
        db_setup('init')

    def build_handlers(self):
        """
        For each recorded response, generates a (path, handler) tuple which
        will be passed to the Tornado web server.
        """
        handlers = []
        handler_builder = HandlerBuilder()
        for path, params in self.responses.items():
            handlers.append((path, handler_builder.get_handler(params)))
        return handlers

    def __getattr__(self, name):
        """
        If the method name matches with set_post_response, set_put_response,
        set_post_response_from_file, etc. generates a dynamic method.
        """
        dynamic_method_matcher = re.match(self.DYNAMIC_METHOD_REGEX, name)
        if dynamic_method_matcher is not None:
            method_name = dynamic_method_matcher.group(1)
            return self.generate_callable_for_set_response(method_name)
        else:
            raise AttributeError("'WebPluginTestCase' object has no attribute '" + name + "'")

    def generate_callable_for_set_response(self, method_name, from_file):
        """Returns a function that will be called to set a response."""
        def dynamic_method(path, content="", headers={}, status_code=200):
            self.set_response(path, content, headers, method_name, status_code)
        return dynamic_method

    def set_response(self, path, content="", headers={}, method="get", status_code=200):
        """
        Sets the response for the server in the given path. Optionally, it
        is possible to specify the headers to be changed, the HTTP method
        to answer to, and the response HTTP status code.
        """
        if not (path in self.responses):
            self.responses[path] = {}
            self.responses[path][method] = {
                "content": content,
                "headers": headers,
                "code": status_code}