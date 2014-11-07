import sys

import unittest
import mock
from hamcrest import *

import owtf


class OWTFCliTest(unittest.TestCase):
    @mock.patch('__builtin__.raw_input', return_value=['Y'])
    @mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
    @mock.patch('owtf.logging.info')
    def test_run_list_plugins(self, log_info, server_start, rvalue):
        """Run OWTF to list the plugins."""
        for cat in ('web', 'net', 'aux'):
            sys.argv = ['owtf.py', '-l', cat]
            try:
                owtf.main(sys.argv)
            except SystemExit:  # Expected behavior (raised by exit())
                pass
            self.assertTrue(
                'Press Ctrl+C' in str(call)
                for call in log_info.call_args_list)
