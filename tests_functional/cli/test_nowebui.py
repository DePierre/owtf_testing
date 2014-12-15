import mock
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliTestCase


class OWTFCliNoWebUITest(OWTFCliTestCase):

    categories = ['cli', 'fast']

    def test_cli_no_webui(self):
        """Run OWTF without its Web UI."""
        self.run_owtf()
        self.assert_has_not_been_logged(
            "http://127.0.0.1:8009 <-- Web UI URL",
            name='MainProcess')
        self.assert_is_in_logs(
            "All jobs have been done. Exiting.",
            name='MainProcess')

    def test_cli_no_webui_again(self):
        """Run OWTF without its Web UI again to check if resources are freed."""
        self.run_owtf()
        self.assert_has_not_been_logged(
            "http://127.0.0.1:8009 <-- Web UI URL",
            name='MainProcess')
        self.assert_is_in_logs(
            "All jobs have been done. Exiting.",
            name='MainProcess')
