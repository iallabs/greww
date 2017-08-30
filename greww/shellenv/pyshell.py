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
    #TODO: Need some documentations
    if cmdline is None:
        raise MissingCommand()
    cmds = _split_cmd(cmdline)
    return subprocess.check_output(cmds, shell=shell, check=check)
