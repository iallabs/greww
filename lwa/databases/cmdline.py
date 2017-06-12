
import sys
#from .databases import LicapyDBManager

command = []

for arg in sys.argv:
    command += [arg]

def build():
    print('build')
    pass

def rebuild():
    print('rebuild')
    pass

def destroy():
    print('destroy')
    pass

def show_content():
    print('show c')
    pass

def show_fields():
    pass

def show_tables():
    pass

def show_database():
    pass

_option = {'--build' : build,
           '--rebuild' : rebuild,
           '--destroy' : destroy,
           '-s' : show_content,
           '-t' : show_tables,
           '-f' : show_fields,
           '-d' : show_database}


class __NotImplementedCommand(Exception):
    pass

def _treat_command_line(cmdargs):
    # [python licapydb.py show databases]
    if not cmdargs[0] in list(_options.keys()):
        raise _NotImplementedCommand('Not implemented cmdline')
    cmd = list(cmdargs)
    return _option[cmd[0]](*cmd[1::])

if __name__ == '__main__':
    print(command)
    print('hello')
    print(_treat_command_line(command))
