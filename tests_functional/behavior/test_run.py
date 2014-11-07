import sys

import unittest
import mock
from hamcrest import *

import owtf


class OWTFRunTest(unittest.TestCase):
    @mock.patch('__builtin__.raw_input', return_value=['Y'])
    @mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
    @mock.patch('owtf.logging.info')
    @mock.patch('owtf.logging.warn')
    def test_run_no_param(self, log_warn, log_info, server_start, rvalue):
        """Run OWTF without any parameter."""
        sys.argv = ['owtf.py', ]
        with self.assertRaises(SystemExit) as cm:
            owtf.main(sys.argv)
        # Check that OWTF exited properly exit(0).
        self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
        # Check that Web UI has started.
        assert_that(str(log_warn.call_args_list), contains_string('Web UI URL'))
        # Check that Web UI has properly started.
        assert_that(str(log_info.call_args_list), contains_string('Press Ctrl+C'))
