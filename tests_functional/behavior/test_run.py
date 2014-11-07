import sys

import unittest
import mock
from hamcrest import *

import owtf


class OWTFTest(unittest.TestCase):
    @mock.patch('__builtin__.raw_input', return_value=['Y'])
    @mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
    @mock.patch('owtf.logging.info')
    def test_run_no_param(self, log_info, server_start, rvalue):
            sys.argv = ['owtf.py', ]
            try:
                owtf.main(sys.argv)
            except SystemExit:  # Expected behavior (raised by exit())
                pass
            self.assertTrue(
                'Press Ctrl+C' in str(call)
                for call in log_info.call_args_list)

    @mock.patch('__builtin__.raw_input', return_value=['Y'])
    @mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
    @mock.patch('owtf.logging.info')
    def test_run_list_web_plugins(self, log_info, server_start, rvalue):
            sys.argv = ['owtf.py', '-l', 'web']
            try:
                owtf.main(sys.argv)
            except SystemExit:  # Expected behavior (raised by exit())
                pass
            self.assertTrue(
                'Press Ctrl+C' in str(call)
                for call in log_info.call_args_list)
