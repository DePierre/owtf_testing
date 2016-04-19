import mock
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliWebPluginTestCase


class OWTFCliTypeTest(OWTFCliWebPluginTestCase):

    categories = ['cli', 'fast']

    def test_cli_type_web_default_active(self):
        """Test OWTF WEB active plugins run by default if no '-g' option specified (regression #390)."""
        self.run_owtf('-s', '-t', 'active', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))
        self.assert_is_in_logs('(web/active', name='Worker', msg='Web active plugins should have been run!')
        self.assert_is_not_in_logs('(web/passive', name='Worker', msg='Web passive plugins should not have been run!')
        self.assert_is_not_in_logs('(web/semi_passive', name='Worker', msg='Web semi passive plugins should not have been run!')
        self.assert_is_not_in_logs('(auxiliary/', name='Worker', msg='Aux plugins should not have been run!')
        self.assert_is_not_in_logs('(network/', name='Worker', msg='Net plugins should not have been run!')
        # Test OWTF exited cleanly.
        self.assert_is_in_logs('All jobs have been done. Exiting.', name='MainProcess')

    def test_cli_type_web_default_passive(self):
        """Test OWTF WEB passive plugins run by default if no '-g' option specified (regression #390)."""
        self.run_owtf('-s', '-t', 'passive', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))
        self.assert_is_in_logs('(web/passive', name='Worker', msg='Web passive plugins should have been run!')
        self.assert_is_not_in_logs('(web/active', name='Worker', msg='Web active plugins should not have been run!')
        self.assert_is_not_in_logs('(web/semi_passive', name='Worker', msg='Web semi passive plugins should not have been run!')
        self.assert_is_not_in_logs('(auxiliary/', name='Worker', msg='Aux plugins should not have been run!')
        self.assert_is_not_in_logs('(network/', name='Worker', msg='Net plugins should not have been run!')
        # Test OWTF exited cleanly.
        self.assert_is_in_logs('All jobs have been done. Exiting.', name='MainProcess')

    def test_cli_type_web_default_semi_passive(self):
        """Test OWTF WEB semi passive plugins run by default if no '-g' option specified (regression #390)."""
        self.run_owtf('-s', '-t', 'semi_passive', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))
        self.assert_is_in_logs('(web/semi_passive', name='Worker', msg='Web semi passive plugins should have been run!')
        self.assert_is_not_in_logs('(web/active', name='Worker', msg='Web active plugins should not have been run!')
        self.assert_is_not_in_logs('(web/passive', name='Worker', msg='Web passive plugins should not have been run!')
        self.assert_is_not_in_logs('(auxiliary/', name='Worker', msg='Aux plugins should not have been run!')
        self.assert_is_not_in_logs('(network/', name='Worker', msg='Net plugins should not have been run!')
        # Test OWTF exited cleanly.
        self.assert_is_in_logs('All jobs have been done. Exiting.', name='MainProcess')

    def test_cli_type_net_default_bruteforce(self):
        """Test OWTF NET bruteforce plugins run by default if no '-g' option specified and target is IP (regression #390)."""
        self.run_owtf('-s', '-t', 'bruteforce', "%s:%s" % (self.IP, self.PORT))
        self.assert_is_in_logs('(web/semi_passive', name='Worker', msg='Web semi passive plugins should have been run!')
        self.assert_is_not_in_logs('(web/active', name='Worker', msg='Web active plugins should not have been run!')
        self.assert_is_not_in_logs('(web/passive', name='Worker', msg='Web passive plugins should not have been run!')
        self.assert_is_not_in_logs('(auxiliary/', name='Worker', msg='Aux plugins should not have been run!')
        self.assert_is_not_in_logs('(network/', name='Worker', msg='Net plugins should not have been run!')
        # Test OWTF exited cleanly.
        self.assert_is_in_logs('All jobs have been done. Exiting.', name='MainProcess')


