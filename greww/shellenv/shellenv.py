from .pyshell import execute_shell_command as esc
import os
# EXPORT AND UNSERT VARS FROM SHELL ENVIRENEMENT

def varenvs():
    cmd = "printenv"
    return esc(cmd, rs=True)

def export_varenv(var, val):
    os.environ[var] = val

def unset_varenv(var):
    del os.environ[var]

def import_varenv(var):
    return os.environ[var]
