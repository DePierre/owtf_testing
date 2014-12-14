import mock
from hamcrest import *
from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliEmptyRunTest(OWTFCliTestCase):

    categories = ['cli', 'fast']

    @log_capture()
    def test_cli_empty_run(self, logger):
        """Run OWTF without parameters."""
        self.run_owtf()
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")
