from .pyshell import execute_shell_command
from greww.utils.strbin import convert_bin_to_str as cbts
from greww.utils.filters import rezip_filter
import os
# EXPORT AND UNSERT VARS FROM SHELL ENVIRENEMENT

esc = execute_shell_command

@rezip_filter(applied_func=cbts)
def varenvs():
    cmd = "printenv"
    return esc(cmd, rs=True)

def _varenvs_keys():
    return varenvs().keys()

def _varenvs_values():
    return varenvs().values()

def all_varenv():
    return os.environ

def export_varenv(var, val):
    os.environ[var] = val

def unset_varenv(var):
    del os.environ[var]

def import_varenv(var):
    return os.environ[var]
