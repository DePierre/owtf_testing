check:
	python -m unittest owtf_testing.tests_functional.cli.test_simulation.OWTFCliSimulationTest.test_cli_simulation
	python -m unittest owtf_testing.tests_functional.cli.test_simulation.OWTFCliSimulationTest.test_cli_no_simulation

	python -m unittest owtf_testing.tests_functional.cli.test_nowebui.OWTFCliNoWebUITest.test_cli_no_webui

	python -m unittest owtf_testing.tests_functional.cli.test_empty_run.OWTFCliEmptyRunTest.test_cli_empty_run

	python -m unittest owtf_testing.tests_functional.cli.test_list_plugins.OWTFCliListPluginsTest.test_cli_list_plugins_aux
	python -m unittest owtf_testing.tests_functional.cli.test_list_plugins.OWTFCliListPluginsTest.test_cli_list_plugins_net
	python -m unittest owtf_testing.tests_functional.cli.test_list_plugins.OWTFCliListPluginsTest.test_cli_list_plugins_web

	python -m unittest owtf_testing.tests_functional.cli.test_only.OWTFCliOnlyPluginsTest.test_only_one_plugin
	python -m unittest owtf_testing.tests_functional.cli.test_only.OWTFCliOnlyPluginsTest.test_only_one_plugin_one_type

	python -m unittest owtf_testing.tests_functional.cli.test_except.OWTFCliExceptTest.test_except

	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_is_valid_ip
	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_is_invalid
	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_is_valid_http
	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_are_mixed
	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_are_mixed_but_web_specified
	python -m unittest owtf_testing.tests_functional.cli.test_scope.OWTFCliScopeTest.test_cli_target_are_mixed_but_net_specified

	# TODO: Deactivated for now. Reactivate when #390 is fixed.
	#python -m unittest owtf_testing.tests_functional.cli.test_type.OWTFCliTypeTest.test_cli_type_web_default_active
	#python -m unittest owtf_testing.tests_functional.cli.test_type.OWTFCliTypeTest.test_cli_type_web_default_passive
	#python -m unittest owtf_testing.tests_functional.cli.test_type.OWTFCliTypeTest.test_cli_type_web_default_semi_passive
	#python -m unittest owtf_testing.tests_functional.cli.test_type.OWTFCliTypeTest.test_cli_type_net_default_bruteforce

	python -m unittest owtf_testing.tests_functional.plugins.web.test_web.OWTFCliWebPluginTest.test_web_active
	python -m unittest owtf_testing.tests_functional.plugins.web.test_web.OWTFCliWebPluginTest.test_web_passive
	python -m unittest owtf_testing.tests_functional.plugins.web.test_web.OWTFCliWebPluginTest.test_web_semi_passive
	python -m unittest owtf_testing.tests_functional.plugins.web.test_web.OWTFCliWebPluginTest.test_web_external
	python -m unittest owtf_testing.tests_functional.plugins.web.test_web.OWTFCliWebPluginTest.test_web_grep

	python -m unittest owtf_testing.tests_functional.plugins.web.active.test_web_active.OWTFCliWebActivePluginTest.test_web_active_wvs_001
	python -m unittest owtf_testing.tests_functional.plugins.web.active.test_web_active.OWTFCliWebActivePluginTest.test_web_active_wvs_006
