import mock
from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFCliTest(OWTFTestCase):

    def test_cli_list_plugins_aux(self):
        """Run OWTF to list the aux plugins."""
        args = ['owtf.py', '-l', 'aux']
        owtf.main(args)
        assert_that(
            str(self.mock_log_info.call_args_list),
            contains_string("Available AUXILIARY plugins"))

    def test_cli_list_plugins_net(self):
        """Run OWTF to list the net plugins."""
        args = ['owtf.py', '-l', 'net']
        owtf.main(args)
        assert_that(
            str(self.mock_log_info.call_args_list),
            contains_string("Available NET plugins"))

    def test_cli_list_plugins_web(self):
        """Run OWTF to list the web plugins."""
        args = ['owtf.py', '-l', 'web']
        owtf.main(args)
        assert_that(
            str(self.mock_log_info.call_args_list),
            contains_string("Available WEB plugins"))
