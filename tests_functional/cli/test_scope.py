import mock
import unittest
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliTestCase


class OWTFCliScopeTest(OWTFCliTestCase):

    categories = ['cli']

    @unittest.skip("Currently broken.")
    def test_cli_target_with_no_protocol(self):
        """Run OWTF with a target but no protocol."""
        self.args += ['%s:%s' % (self.IP, self.PORT)]
        self.run_owtf()
        self.assert_is_in_logs("#TODO")

    def test_cli_target_is_invalid(self):
        """Run OWTF with an invalid target."""
        invalid_target = 'a' * 63 + '.invalid'
        self.run_owtf('%s://%s' % (self.PROTOCOL, invalid_target))
        self.assert_is_in_logs(
            "Unable to resolve: '%s'" % invalid_target,
            name='MainProcess')

    def test_cli_target_is_valid_http(self):
        """Run OWTF with a valid http target."""
        self.run_owtf('-s', '%s://%s:%s' % (self.PROTOCOL, self.IP, self.PORT))
        self.assert_is_in_logs(
            "All jobs have been done. Exiting.",
            name='MainProcess')
