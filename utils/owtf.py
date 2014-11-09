import os
import sys
import subprocess

import unittest
import mock
from hamcrest import *


class OWTFTestCase(unittest.TestCase):

    DIR_SCRIPTS = 'scripts'
    DB_SETUP_SCRIPT = 'db_setup.sh'

    def setUp(self):
        # Reset the database.
        self.db_setup('clean')
        self.db_setup('init')
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
        # Reset the database.
        self.db_setup('clean')
        self.db_setup('init')

    @classmethod
    def db_setup(cls, cmd):
        if cmd not in ['clean', 'init']:
            return
        pwd = os.getcwd()
        # TODO: Make backup of the db or change the db directory,
        # otherwise user's database will be deleted.
        db_process = subprocess.Popen(
            "/usr/bin/echo '\n' | %s %s" % (
                os.path.join(pwd, cls.DIR_SCRIPTS, cls.DB_SETUP_SCRIPT),
                cmd),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        db_process.wait()
