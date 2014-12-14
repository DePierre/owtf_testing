from owtf_testing.tests_functional.cli.test_empty_run import OWTFCliEmptyRunTest
from owtf_testing.tests_functional.cli.test_list_plugins import OWTFCliListPluginsTest
from owtf_testing.tests_functional.cli.test_nowebui import OWTFCliNoWebUITest
from owtf_testing.tests_functional.cli.test_scope import OWTFCliScopeTest
from owtf_testing.tests_functional.cli.test_simulation import OWTFCliSimulationTest


SUITES = [
    OWTFCliEmptyRunTest,
    OWTFCliListPluginsTest,
    OWTFCliNoWebUITest,
    OWTFCliScopeTest,
    OWTFCliSimulationTest
]
