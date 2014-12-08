import mock
from hamcrest import *
from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliEmptyRunTest(OWTFCliTestCase):

    @log_capture()
    def test_cli_no_webui(self, logger):
        """Run OWTF without its Web UI."""
        self.run_owtf()
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")

    @log_capture()
    def test_cli_with_target(self, logger):
        """Run OWTF with a target."""
        self.args += ['%s://%s:%s' % (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()
        self.assert_has_been_logged(
            logger,
            "The IP address for %s is: '%s'" % (self.IP, self.IP))

    @log_capture()
    def test_cli_with_target_twice(self, logger):
        """Run OWTF with a target twice."""
        # Add the target twice and check that OWTF use the database to retrieve
        # the IP address of the target when checking the second one.
        self.args += ['%s://%s:%s' % (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()
        self.assert_has_been_logged(
            logger,
            "%s://%s:%s already exists in DB" % (self.PROTOCOL, self.IP, self.PORT))
