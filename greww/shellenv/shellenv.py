from .pyshell import execute_shell_command as esc
# EXPORT AND UNSERT VARS FROM SHELL ENVIRENEMENT

"""
>export value1="amineis feeding his ass"
>echo $value1
amineis feeding his ass
>unset value1
>echo $value1
-bash value1: command not found
"""

def export_varenv(var, val):
    cmd = "export {0}={1}".format(var, val)
    esc(cmd, rs=True)

def unset_varenv(var):
    cmd = "unset {0}".format(var)
    esc(cmd)

def import_varenv(var):
    cmd = "echo ${0}".format(var)
    return esc(cmd, rs=True)
