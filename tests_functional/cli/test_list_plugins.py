import mock
from hamcrest import *

from owtf_testing.utils.owtftest import OWTFCliTestCase


@mock.patch('framework.plugin.plugin_handler.PluginHandler.ShowPluginTypePlugins')
class OWTFCliListPluginsTest(OWTFCliTestCase):

    def test_cli_list_plugins_aux(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the aux plugins."""
        self.args += ['-l', 'aux']
        group = 'aux'
        types = ['exploit', 'smb', 'bruteforce', 'dos', 'wafbypasser', 'se', 'rce', 'selenium']
        self.run_owtf()

        self.assert_show_plugin_type_plugins_called_with(
            mock_show_plugin_type_plugins,
            types, group)

    def test_cli_list_plugins_net(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the net plugins."""
        self.args += ['-l', 'net']
        group = 'net'
        types = ['active', 'bruteforce']
        self.run_owtf()

        self.assert_show_plugin_type_plugins_called_with(
            mock_show_plugin_type_plugins,
            types, group)

    def test_cli_list_plugins_web(self, mock_show_plugin_type_plugins):
        """Run OWTF to list the web plugins."""
        self.args += ['-l', 'web']
        group = 'web'
        types = ['external', 'active', 'passive', 'grep', 'semi_passive']
        self.run_owtf()

        self.assert_show_plugin_type_plugins_called_with(
            mock_show_plugin_type_plugins,
            types, group)

    @classmethod
    def assert_show_plugin_type_plugins_called_with(cls, mock_obj, plugin_types, plugin_group):
        for plugin_type in plugin_types:
            cls.assert_called_with(mock_obj, plugin_type, plugin_group)
