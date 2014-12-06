import mock
from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFCliTest(OWTFTestCase):

    @mock.patch('framework.plugin.plugin_handler.PluginHandler.ShowPluginTypePlugins')
    def test_cli_list_plugins_aux(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the aux plugins."""
        args = ['owtf.py', '-l', 'aux']
        owtf.main(args)
        # Check plugin group.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'aux'"))
        # Check plugin types.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'exploit'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'smb'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'bruteforce'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'dos'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'wafbypasser'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'se'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'rce'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'selenium'"))

    @mock.patch('framework.plugin.plugin_handler.PluginHandler.ShowPluginTypePlugins')
    def test_cli_list_plugins_net(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the net plugins."""
        args = ['owtf.py', '-l', 'net']
        owtf.main(args)
        # Check plugin group.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'net'"))
        # Check plugin types.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'active'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'bruteforce'"))

    @mock.patch('framework.plugin.plugin_handler.PluginHandler.ShowPluginTypePlugins')
    def test_cli_list_plugins_web(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the web plugins."""
        args = ['owtf.py', '-l', 'web']
        owtf.main(args)
        # Check plugin group.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'web'"))
        # Check plugin types.
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'external'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'active'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'passive'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'grep'"))
        assert_that(
            str(mock_show_plugin_type_plugins.call_args_list),
            contains_string("'semi_passive'"))
