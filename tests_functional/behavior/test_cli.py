import sys

from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFCliTest(OWTFTestCase):
    def test_run_list_plugins(self):
        """Run OWTF to list the plugins."""
        for cat in ('web', 'net', 'aux'):
            sys.argv = ['owtf.py', '-l', cat]
            try:
                owtf.main(sys.argv)
            except SystemExit:  # Expected behavior (raised by exit())
                pass
            assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))
