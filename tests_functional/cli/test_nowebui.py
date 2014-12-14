import mock
from hamcrest import *

from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliNoWebUITest(OWTFCliTestCase):

    categories = ['cli', 'fast']

    @log_capture()
    def test_cli_no_webui(self, logger):
        """Run OWTF without its Web UI."""
        self.run_owtf()
        self.assert_has_not_been_logged(
            logger,
            "http://127.0.0.1:8009 <-- Web UI URL")
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")

    @log_capture()
    def test_cli_no_webui_again(self, logger):
        """Run OWTF without its Web UI again to check if resources are freed."""
        self.run_owtf()
        self.assert_has_not_been_logged(
            logger,
            "http://127.0.0.1:8009 <-- Web UI URL")
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")
