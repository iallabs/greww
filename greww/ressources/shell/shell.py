# execute shell command lines
from greww.utils.exceptions import MissingCommand
import subprocess

#TODO
def _split_cmd(cmdline):
    """
    """
    return [i for i in cmdline.split(' ')]

def execute_shell_command(cmdline=None, shell=False, check=False, rs=False, **kwargs):
    """
    Execute shell command at shell subprocess
    with rs=False : the function return the command line result
    """
    if cmdline is None:
        raise MissingCommand()
    cmds = _split_cmd(cmdline)
    if not rs:
        subprocess.run(cmds, shell=shell, check=check)
    else:
        return subprocess.run(cmds, shell=shell, check=check, stdout=subprocess.PIPE).stdout.split(b'\n')

def shell_command_output(cmdline=None, shell=False, check=False):
    """
    Not working just use execute_shell_command with rs=True
    """
    if cmdline is None:
        raise MissingCommand()
    cmds = _split_cmd(cmdline)
    return subprocess.check_output(cmds, shell=shell, check=check)


#NOTE: to understand this part take a look at
# https://stackoverflow.com/questions/17904231/handling-tcpdump-output-in-python

def catch_shell_streaming(cmdline=None,
                          verbose=False,
                          to_file=None,
                          __func=None,
                          with_runtime_limit=None,
                          with_iterations_limit=None,
                          with_datetime_limit=None):
    """
    Cant read shell command lines that stream data like tcpdump / top
    """
    #TODO runtime / iterations / datetime limit
    #NOTE STILL NOT TESTED
    cmds = _split_cmd(cmdline)
    p = subprocess.Popen(cmds, stdout=sub.PIPE)
    if verbose:
        for row in iter(p.stdout.readline, b''):
            print(row.rstrip())   # process here
    elif to_file:
        f = open(to_file, 'w')
        for row in iter(p.stdout.readline, b''):
            f.write(row)
        f.close()
    elif __func:
        for row in iter(p.stdout.readline, b''):
            __func(row)
    else:
        __func = lambda x : print(x)
        for row in iter(p.stdout.readline, b''):
            __func(row)


class Shell(object):
    """
    Shell execution and envirenement
    """
    slots = []

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
