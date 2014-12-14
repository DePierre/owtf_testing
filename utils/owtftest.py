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
from owtf_testing.utils.service.web.server import WebServerProcess

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
    def assert_has_not_been_logged(logger, msg):
        """Assert that ``msg`` was not logged by ``logger``."""
        messages = [record.msg for record in logger.records]
        assert_that(messages, not(has_item(msg)))

    @staticmethod
    def assert_is_in_logs(logger, msg):
        """Assert that ``msg`` is part of a message logged by ``logger``."""
        messages = [record.msg for record in logger.records]
        assert_that(str(messages), contains_string(msg))

    @staticmethod
    def assert_is_not_in_logs(logger, msg):
        """Assert that ``msg`` is not part of a message logged by ``logger``."""
        messages = [record.msg for record in logger.records]
        assert_that(str(messages), not(contains_string(msg)))

    @staticmethod
    def assert_are_in_logs(logger, msgs):
        """Assert that each message of ``msgs`` is part of a message logged by ``logger``."""
        for msg in msgs:
            OWTFCliTestCase.assert_is_in_logs(logger, msg)

    @staticmethod
    def assert_are_not_in_logs(logger, msgs):
        """Assert that each message of ``msgs`` is not part of a message logged by ``logger``."""
        for msg in msgs:
            OWTFCliTestCase.assert_is_not_in_logs(logger, msg)

    @staticmethod
    def assert_called_with(mock_obj, *args):
        """Assert that ``mock_obj`` has been called with all elements from
        ``args`` (in order).
        """
        mock_obj.assert_any_call(*args)


class OWTFCliWebPluginTestCase(OWTFCliTestCase):

    DEFAULT_ARGS = ['owtf.py', '--nowebui']
    PROTOCOL = 'http'
    IP = '127.0.0.1'
    PORT = '8888'
    MATCH_PLUGIN_START = 'Execution Start'
    MATCH_BUG = 'OWTF BUG'
    DYNAMIC_METHOD_REGEX = "^set_(head|get|post|put|delete|options|connect)_response"

    def setUp(self):
        super(OWTFCliWebPluginTestCase, self).setUp()
        # Web server initialization.
        self.server = WebServerProcess(self.IP, self.PORT)
        self.server.start()

    def tearDown(self):
        self.server.stop()
