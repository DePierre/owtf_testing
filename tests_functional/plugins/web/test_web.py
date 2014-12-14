import mock
from hamcrest import *
from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliWebPluginTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliWebPluginTest(OWTFCliWebPluginTestCase):

    categories = ['plugins', 'web']

    @log_capture()
    def test_web_active(self, logger):
        """Test OWTF WEB active plugins."""
        self.run_owtf('-g', 'web', '-t', 'active', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))

    @log_capture()
    def test_web_passive(self, logger):
        """Test OWTF WEB passive plugins."""
        self.run_owtf('-g', 'web', '-t', 'passive', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))

    @log_capture()
    def test_web_semi_passive(self, logger):
        """Test OWTF WEB semi-passive plugins."""
        self.run_owtf('-g', 'web', '-t', 'semi_passive', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))

    @log_capture()
    def test_web_external(self, logger):
        """Test OWTF WEB external plugins."""
        self.run_owtf('-g', 'web', '-t', 'external', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))

    @log_capture()
    def test_web_grep(self, logger):
        """Test OWTF WEB grep plugins."""
        self.run_owtf('-g', 'web', '-t', 'grep', "%s://%s:%s" % (self.PROTOCOL, self.IP, self.PORT))
