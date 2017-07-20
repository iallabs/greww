# execute shell command lines
from greww.utils.exceptions import MissingCommand
import subprocess


def _split_cmd(cmdline):
    return [i for i in cmdline.split(' ')]


def execute_shell_command(cmdline=None, shell=False, check=False, rs=False, **kwargs):
    if cmdline is None:
        raise MissingCommand()
    cmds = _split_cmd(cmdline)
    if not rs:
        subprocess.run(cmds, shell=shell, check=check)
    else:
        return subprocess.run(cmds, shell=shell, check=check, stdout=subprocess.PIPE).stdout.split(b'\n')

def shell_command_output(cmdline=None, shell=False, check=False):
    if cmdline is None:
        raise MissingCommand()
    cmds = _split_cmd(cmdline)
    return subprocess.check_output(cmds, shell=shell, check=check)
