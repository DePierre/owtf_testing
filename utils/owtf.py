import sys

import unittest
import mock
from hamcrest import *


class OWTFTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_input_patcher = mock.patch('__builtin__.raw_input', return_value=['Y'])
        self.interface_server_patcher = mock.patch('framework.interface.server.InterfaceServer.start', side_effect=KeyboardInterrupt)
        self.log_info_patcher = mock.patch('owtf.logging.info')
        self.log_warn_patcher = mock.patch('owtf.logging.warn')
        self.raw_input_patcher.start()
        self.interface_server_patcher.start()
        self.mock_log_info = self.log_info_patcher.start()
        self.mock_log_warn = self.log_warn_patcher.start()

    def tearDown(self):
        self.raw_input_patcher.stop()
        self.interface_server_patcher.stop()
        self.log_info_patcher.stop()
        self.log_warn_patcher.stop()
