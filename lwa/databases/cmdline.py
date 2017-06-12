
import sys
#from .databases import LicapyDBManager

from lwa.databases.databases import LicapyDBManager

_lic = LicapyDBManager(cnxargs=('localhost', 'root', 'uehMLMRw', ''))

command = []

for arg in sys.argv:
    command += [arg]

def build():
    _lic._build_db()
    _lic._build_all_architecture()

def rebuild():
    _lic._rebuild_database

def destroy():
    _lic._destroy_all()

def show_content(*args):
    a = list(args)
    if len(a) == 2:
        m, n = a[0], a[1]
        _lic.use_database(m)
        _lic._show_table(n, show=True)
    return False

def show_fields(*args):
    pass

def show_tables(*args):
    pass

def show_database(*args):
    pass

def state():
    pass

def search():
    pass

_option = {'--build' : build,
           '--rebuild' : rebuild,
           '--destroy' : destroy,
           '--state' : state,
           '--search' : search,
           '-s' : show_content,
           '-t' : show_tables,
           '-f' : show_fields,
           '-d' : show_database}


class __NotImplementedCommand(Exception):
    pass

def _treat_command_line(cmdargs):
    # [python licapydb.py show databases]
    if not cmdargs[1] in list(_option.keys()):
        raise _NotImplementedCommand('Not implemented cmdline')
    cmd = list(cmdargs)
    return _option[cmd[1]](*cmd[2::])

if __name__ == '__main__':
    print(command)
    print('hello')
    print(_treat_command_line(command))
