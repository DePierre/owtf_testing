import os
import re
import sys
import copy
import logging
import subprocess

import unittest
import mock
from hamcrest import *

from owtf_testing.utils.clean import db_setup, clean_owtf_review
from owtf_testing.utils.service.web.server import WebServerProcess, HandlerBuilder

import owtf


class OWTFCliTestCase(unittest.TestCase):

    """Basic OWTF test case that initialises basic patches."""

    DEFAULT_ARGS = ['owtf.py', '--nowebui']
    PROTOCOL = 'http'
    IP = '127.0.0.1'
    PORT = '8888'

    def __init__(self, methodName='runTest'):
        super(OWTFCliTestCase, self).__init__(methodName)
        self.args = copy.copy(self.DEFAULT_ARGS)

    def setUp(self):
        self.args = copy.copy(self.DEFAULT_ARGS)
        self.clean_old_runs()
        self.raw_input_patcher = mock.patch('__builtin__.raw_input', return_value=['Y'])
        self.raw_input_patcher.start()

    def tearDown(self):
        self.raw_input_patcher.stop()

    ###
    # OWTF utils methods.
    ###

    def run_owtf(self, *extra_args):
        """Run OWTF with args plus ``extra_args`` if any."""
        if self.args:
            args = self.args[:]
        else:
            args = self.DEFAULT_ARGS[:]
        if extra_args:
            args += extra_args
        owtf.main(args)

    @staticmethod
    def clean_old_runs():
        """Clean the database and the older owtf_review directory."""
        # Reset the database.
        db_setup('clean')
        db_setup('init')
        # Remove old OWTF outputs
        clean_owtf_review()

    ###
    # Specific methods that test logs and function calls.
    ###

    @staticmethod
    def assert_has_been_logged(logger, msg):
        """Assert that ``msg`` was logged by ``logger``."""
        messages = [record.msg for record in logger.records]
        assert_that(messages, has_item(msg))

    @staticmethod
    def assert_is_in_logs(logger, msg):
        """Assert that ``msg`` is part of a message logged by ``logger``."""
        messages = [record.msg for record in logger.records]
        assert_that(str(messages), contains_string(msg))

    @staticmethod
    def assert_are_in_logs(logger, msgs):
        """Assert that each message of ``msgs`` is part of a message logged by ``logger``."""
        for msg in msgs:
            OWTFCliTestCase.assert_is_in_logs(logger, msg)

    @staticmethod
    def assert_called_with(mock_obj, *args):
        """Assert that ``mock_obj`` has been called with all elements from
        ``args`` (in order).
        """
        mock_obj.assert_any_call(*args)


class OWTFCliWebPluginTestCase(OWTFCliTestCase):

    PROTOCOL = 'http'
    IP = '127.0.0.1'
    PORT = '8888'
    MATCH_PLUGIN_START = 'Execution Start'
    MATCH_BUG = 'OWTF BUG'
    DYNAMIC_METHOD_REGEX = "^set_(head|get|post|put|delete|options|connect)_response"

    def setUp(self):
        super(OWTFCliWebPluginTestCase, self).setUp()
        # Web server initialization.
        self.responses = {}
        self.server = WebServerProcess(self.IP, self.PORT, self.build_handlers())
        self.server.start()

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
