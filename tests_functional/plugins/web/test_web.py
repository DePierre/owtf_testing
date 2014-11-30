import mock
from hamcrest import *

from owtf_testing.utils.owtf import OWTFWebPluginTestCase
import owtf


class OWTFWebPluginTest(OWTFWebPluginTestCase):

    def test_web_active(self):
        """Test OWTF WEB active plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'active', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        owtf.main(args)
