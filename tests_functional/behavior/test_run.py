import sys

import unittest
import mock
from hamcrest import *

import owtf


class OWTFRunTest(unittest.TestCase):
    @mock.patch('__builtin__.raw_input', return_value=['Y'])
    @mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
    @mock.patch('owtf.logging.warn')
    @mock.patch('owtf.logging.info')
    def test_run_no_param(self, log_info, log_warn, server_start, rvalue):
        """Run OWTF without any parameter."""
        sys.argv = ['owtf.py', ]
        try:
            owtf.main(sys.argv)
        except SystemExit:  # Expected behavior (raised by exit())
            pass
        self.assertTrue(
            'Web UI URL' in str(call)
            for call in log_warn.call_args_list)
        self.assertTrue(
            'Press Ctrl+C' in str(call)
            for call in log_info.call_args_list)
