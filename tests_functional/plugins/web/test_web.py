import unittest
import mock
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliWebPluginTestCase


@unittest.skip("Currently broken.")
class OWTFCliWebPluginTest(OWTFCliWebPluginTestCase):

    def test_web_active(self):
        """Test OWTF WEB active plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'active', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()

    def test_web_passive(self):
        """Test OWTF WEB passive plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'passive', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()

    def test_web_semi_passive(self):
        """Test OWTF WEB semi-passive plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'semi_passive', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()

    def test_web_external(self):
        """Test OWTF WEB external plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'external', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()

    def test_web_grep(self):
        """Test OWTF WEB grep plugins."""
        args = [
            'owtf.py', '-g', 'web', '-t', 'grep', "%s://%s:%s" %
            (self.PROTOCOL, self.IP, self.PORT)]
        self.run_owtf()
