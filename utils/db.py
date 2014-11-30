import os
import subprocess


DIR_SCRIPTS = 'scripts'
DB_SETUP_SCRIPT = 'db_setup.sh'


def db_setup(cmd):
    if cmd not in ['clean', 'init']:
        return
    pwd = os.getcwd()
    # TODO: Make backup of the db or change the db directory,
    # otherwise user's database will be deleted.
    db_process = subprocess.Popen(
        "/usr/bin/echo '\n' | %s %s" % (
            os.path.join(pwd, DIR_SCRIPTS, DB_SETUP_SCRIPT),
            cmd),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    db_process.wait()
