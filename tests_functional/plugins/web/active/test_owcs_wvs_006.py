import mock
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliWebPluginTestCase


class OWTFCliWebActiveWVS006PluginTest(OWTFCliWebPluginTestCase):

    categories = ['plugins', 'web', 'owtf-wvs-006', 'fast']

    def test_web_active(self):
        """Test OWTF WEB active plugins."""
        self.run_owtf('-o', 'OWTF-WVS-006', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))
        # Test Skipfish went OK.
        self.assert_is_in_logs(
            '1 - Target: http://127.0.0.1:8888 -> Plugin: Skipfish Unauthenticated (active)',
            name='Worker')
        self.assert_is_in_logs('This was a great day for science!', name='Worker')
        self.assert_is_in_logs('Execution Start Date/Time:', name='Worker')
        # Test no other plugin has been run.
        self.assert_is_not_in_logs('2 - Target:', name='Worker')
        # Test OWTF exited cleanly.
        self.assert_is_in_logs('All jobs have been done. Exiting.', name='MainProcess')
