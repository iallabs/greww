from .shellenv import unset_varenv, export_varenv, import_varenv
from .pyshell import execute_shell_command as esc

class VarEnv(object):
    """
    Fast shell variables manipulations
    Do not use this in long programing scripts
    use direct functions instead
    """
    slots = []

    @staticmethod
    def unset(var):
        unset_varenv(var)

    @staticmethod
    def export(var, val):
        export_varenv(var, val)

    @staticmethod
    def value(var):
        import_varenv(var)


class Shell(object):
    """
    Shell execution and envirenement
    """
    slots = []
    var = VarEnv

    @staticmethod
    def execute(*args, **kwargs):
        return esc(*args, **kwargs)

    #XXX: declared as var=VarEnv instead
    # Just to not use '()' for nothing
    #@staticmethod
    #def var():
    #    return VarEnv
    @staticmethod
    def execute_under_new_popen():
        """
        Not Implemented
        """
        raise NotImplemented()
