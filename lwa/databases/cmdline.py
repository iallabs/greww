
import sys
from .databases import LicapyDBManager

command = []

for arg in sys.argv:
    command += [arg]

_option = ['--build', '--destroy', 'show' , 'fields', 'select', 'db']

class __NotImplementedCommand(Exception):
    pass

def _treat_command_line(cmdargs):
    # [python licapydb.py show databases]
    if not cmd[0] in _options:
        raise _NotImplementedCommand('Not implemented cmdline')
    return 'yes'

if __name__ == '__main__':
    print(command)
    print('hello')
    print(_treat_command_line(command))
