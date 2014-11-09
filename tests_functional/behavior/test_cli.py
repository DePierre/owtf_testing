import sys

import mock
from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFCliTest(OWTFTestCase):
    @mock.patch('framework.interface.server.FileServer')
    @mock.patch('framework.plugin.worker_manager.Worker')
    def test_run_list_plugins(self, mock_worker, mock_fileserver):
        """Run OWTF to list the plugins."""
        for cat in ('web', 'net', 'aux'):
            sys.argv = ['owtf.py', '-l', cat]
            # Force empty tasks for workers.
            mock_worker.input_q.get.return_value = ()
            with self.assertRaises(SystemExit) as cm:
                owtf.main(sys.argv)
            # Check that OWTF exited properly exit(0).
            self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
            # Check that Web UI has properly started.
            assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))
