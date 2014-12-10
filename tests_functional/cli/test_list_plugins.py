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
        expected = ['Available AUXILIARY plugins', 'exploit', 'smb', 'bruteforce', 'dos', 'wafbypasser', 'se', 'rce', 'selenium']

        self.run_owtf('-l', 'aux')
        self.assert_are_in_logs(logger, expected)
        self.run_owtf('--list_plugins', 'aux')
        self.assert_are_in_logs(logger, expected)

    @log_capture()
    def test_cli_list_plugins_net(self, logger):
        """Run OWTF to list the net plugins."""
        expected = ['Available NET plugins', 'active', 'bruteforce']

        self.run_owtf('-l', 'net')
        self.assert_are_in_logs(logger, expected)
        self.run_owtf('--list_plugins', 'net')
        self.assert_are_in_logs(logger, expected)

    @log_capture()
    def test_cli_list_plugins_web(self, logger):
        """Run OWTF to list the web plugins."""
        expected = ['Available WEB plugins', 'external', 'active', 'passive', 'grep', 'semi_passive']

        self.run_owtf('-l', 'web')
        self.assert_are_in_logs(logger, expected)
        self.run_owtf('--list_plugins', 'web')
        self.assert_are_in_logs(logger, expected)
