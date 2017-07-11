import os
import argparse
#from .mysql_utils import ()

def main():
    vm=None
    table=None
    tb=None
    db=None
    expand=None
    tcontent=False
    content=False
    sl = None

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--info', action="store_true", default=False)
    parser.add_argument('-vm', '--virtualmachine', type=str)
    parser.add_argument('-tb', '--table', type=str)
    parser.add_argument('-db', '--database', type=str)
    parser.add_argument('-X', '--expand', action="store_true", default=False)
    parser.add_argument('-sl', '--selection', type=str)
    parser.add_argument('-sio', '--serviceio', action="store_true", default=False)
    args = parser.parse_args()

    vm = args.virtualmachine
    db = args.database
    tb = args.table
    sl = args.selection

    if args.info:
        if args.virtualmachine:
            if args.database:
                if args.table:
                    pretty_info(instance=vm, db=db, table=table, expand=args.expand)
                    return
                pretty_info(instance=vm, db=db, expand=args.expand)
                return
            pretty_info(instance=vm, expand=args.expand)
            return
        return

    elif args.serviceio:
        if args.virtualmachine:
            if args.database:
                if args.table:
                    if args.selection:
                        _us1(select_from_table(instance=vm, db=db, table=tb, wstm=sl))
                        return
                    _us1(table_fields(instance=vm, db=db, table=tb))
                    return
                _us1(instance_tables(instance=vm, db=db))
                return
            _us1(instance_databases(instance=vm))
            return
        print('options -vm -db -tb -sl')
        return


def _code_kwargs(**kwargs):
    pass

def _decode_sn(sn):
    pass

def _us0(*args):
    # use to output list or tuple of data as one string
    # contaning all it elements seperated by comas ','
    targs = list(args)
    op = str(targs[0])
    for a in targs[1::]:
        op += ',' + a
    print(op)

def _us1(ln):
    for i in ln:
        print(i)

def print_pretty_databases(instance=None, with_tables=False):
    print(' #------------------ DATABASES')
    print('')
    for db in instance_databases(instance=instance):
        print(' #------------------', db)
        if with_tables:
            print_pretty_tables(instance=instance, db=db)

def print_pretty_tables(instance=None, db=None):
    print(' #---------------------------- : TABLES')
    print('')
    for tb in instance_tables(instance=instance, db=db):
        print(' #---------------------------- : ' + tb)

def print_pretty_content(instance=None, db=None, table=None):
    print('kaka')

def print_pretty_fields(instance=None, db=None, table=None):
    print(table_fields(instance=instance, db=db, table=table))

def pretty_info(instance=None, db=None, table=None, expand=False):
    if instance:
        print(' #-- VM : ', instance)
        print('')
        if db:
            print(' #------------- : ', db)
            print('')
            if table:
                print(' #----------------- : ', table)
                print_pretty_fields(instance=instance, db=db, table=table)
                if expand:
                    #print_pretty_content(instance=instance, db=db, table=table)
                    print('not expand for this option -i -vm -tb')
            else:
                if expand:
                    print('not expand for this option -i -vm -db')
                else:
                    print_pretty_tables(instance=instance, db=db)
        else:
            if expand:
                print_pretty_databases(instance=instance, with_tables=True)
            else:
                print_pretty_databases(instance=instance)

if __name__ == "__main__":
    main()
