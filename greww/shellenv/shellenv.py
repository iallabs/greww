from .pyshell import execute_shell_command
import os
# EXPORT AND UNSERT VARS FROM SHELL ENVIRENEMENT

esc = execute_shell_command

def varenvs():
    cmd = "printenv"
    return esc(cmd, rs=True)

def export_varenv(var, val):
    os.environ[var] = val

def unset_varenv(var):
    del os.environ[var]

def import_varenv(var):
    return os.environ[var]
