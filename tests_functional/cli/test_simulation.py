import mock
from testfixtures import log_capture

from owtf_testing.utils.utils import dummy
from owtf_testing.utils.owtftest import OWTFCliTestCase

from framework.core import Core
from framework.dependency_management.dependency_resolver import ServiceLocator


@mock.patch.object(Core, 'enable_logging', dummy)
class OWTFCliSimulationTest(OWTFCliTestCase):

    categories = ['cli', 'fast']

    @log_capture()
    def test_cli_simulation(self, logger):
        """Run OWTF in simulation mode."""
        self.run_owtf('-s')
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")
        plugin_handler = ServiceLocator.get_component("plugin_handler")
        self.assertTrue(plugin_handler.Simulation)

    @log_capture()
    def test_cli_no_simualtion(self, logger):
        """Run OWTF not in simulation mode."""
        self.run_owtf()
        self.assert_has_been_logged(logger, "All jobs have been done. Exiting.")
        plugin_handler = ServiceLocator.get_component("plugin_handler")
        self.assertFalse(plugin_handler.Simulation)
