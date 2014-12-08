import mock
from hamcrest import *

from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliListPluginsTest(OWTFCliTestCase):

    @log_capture()
    def test_cli_list_plugins_aux(self, logger):
        """Run OWTF to list the aux plugins."""
        self.args += ['-l', 'aux']
        expected = ['Available AUXILIARY plugins', 'exploit', 'smb', 'bruteforce', 'dos', 'wafbypasser', 'se', 'rce', 'selenium']
        self.run_owtf()

        self.assert_are_in_logs(logger, expected)

    @log_capture()
    def test_cli_list_plugins_net(self, logger):
        """Run OWTF to list the net plugins."""
        self.args += ['-l', 'net']
        expected = ['Available NET plugins', 'active', 'bruteforce']
        self.run_owtf()

        self.assert_are_in_logs(logger, expected)

    @log_capture()
    def test_cli_list_plugins_web(self, logger):
        """Run OWTF to list the web plugins."""
        self.args += ['-l', 'web']
        expected = ['Available WEB plugins', 'external', 'active', 'passive', 'grep', 'semi_passive']
        self.run_owtf()

        self.assert_are_in_logs(logger, expected)
