import sys

import mock
from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFRunTest(OWTFTestCase):
    @mock.patch('framework.interface.server.FileServer')
    @mock.patch('framework.plugin.worker_manager.Worker')
    def test_run_no_param(self, mock_worker, mock_fileserver):
        """Run OWTF with no parameter."""
        sys.argv = ['owtf.py', ]
        # Force empty tasks for workers.
        mock_worker.input_q.get.return_value = ()
        mock_fileserver.server.start.side_effect = KeyboardInterrupt
        with self.assertRaises(SystemExit) as cm:
            owtf.main(sys.argv)
        # Check that OWTF exited properly exit(0).
        self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
        # Check that Web UI has started.
        assert_that(str(self.mock_log_warn.call_args_list), contains_string('Web UI URL'))
        # Check that Web UI has properly started.
        assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))

    @mock.patch('framework.config.config.cprint')
    @mock.patch('framework.interface.server.FileServer')
    @mock.patch('framework.plugin.worker_manager.Worker')
    def test_run_with_target(self, mock_worker, mock_fileserver, mock_cprint):
        """Run OWTF with a target."""
        sys.argv = ['owtf.py', '-s', 'http://127.0.0.1']
        # Force empty tasks for workers.
        mock_worker.input_q.get.return_value = ()
        mock_fileserver.server.start.side_effect = KeyboardInterrupt
        with self.assertRaises(SystemExit) as cm:
            owtf.main(sys.argv)
        # Check that OWTF exited properly exit(0).
        self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
        assert_that(
            str(mock_cprint.call_args_list),
            contains_string("The IP address for 127.0.0.1 is: '127.0.0.1'"))
        # Check that Web UI has started.
        assert_that(str(self.mock_log_warn.call_args_list), contains_string('Web UI URL'))
        # Check that Web UI has properly started.
        assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))

    @mock.patch('framework.config.config.cprint')
    @mock.patch('framework.interface.server.FileServer')
    @mock.patch('framework.plugin.worker_manager.Worker')
    def test_run_with_target_twice(self, mock_worker, mock_fileserver, mock_cprint):
        """Run OWTF with a target twice."""
        sys.argv = ['owtf.py', '-s', 'http://127.0.0.1']
        # Force empty tasks for workers.
        mock_worker.input_q.get.return_value = ()
        mock_fileserver.server.start.side_effect = KeyboardInterrupt
        with self.assertRaises(SystemExit) as cm:
            owtf.main(sys.argv)
        # Check that OWTF exited properly exit(0).
        self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
        assert_that(
            str(mock_cprint.call_args_list),
            contains_string("http://127.0.0.1 already exists in DB"))
        # Check that Web UI has started.
        assert_that(str(self.mock_log_warn.call_args_list), contains_string('Web UI URL'))
        # Check that Web UI has properly started.
        assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))
