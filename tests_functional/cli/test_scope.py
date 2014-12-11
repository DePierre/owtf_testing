import mock
import unittest
from hamcrest import *
from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliScopeRunTest(OWTFCliTestCase):

    @unittest.skip("Currently broken.")
    @log_capture()
    def test_cli_target_with_no_protocol(self, logger):
        """Run OWTF with a target but no protocol."""
        self.args += ['%s:%s' % (self.IP, self.PORT)]
        self.run_owtf()
        self.assert_has_been_logged(logger, "#TODO")

    @log_capture()
    def test_cli_target_is_invalid(self, logger):
        """Run OWTF with an invalid target."""
        invalid_target = 'a' * 63 + '.invalid'
        self.run_owtf('%s://%s' % (self.PROTOCOL, invalid_target))
        self.assert_has_been_logged(
            logger,
            "Unable to resolve: '%s'" % invalid_target)

    @log_capture()
    def test_cli_target_is_valid_http(self, logger):
        """Run OWTF with a valid http target."""
        self.run_owtf('-s', '%s://%s:%s' % (self.PROTOCOL, self.IP, self.PORT))
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")
