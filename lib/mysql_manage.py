from lib.utils.decorators import _firstraws
from lib.mysql_connect import mysql_connect, THIS_INSTANCE
from lib.mysql_logs import get_db_architecture

import argparse

def main():
    vm=None
    table=None
    tb=None
    db=None
    expand=None
    tcontent=False
    content=False
    parser = argparse.ArgumentParser()
    parser.add_argument('-vm', '--virtualmachine', type=str, default=THIS_INSTANCE)
    parser.add_argument('-i', '--info', action="store_true", default=False)
    parser.add_argument('-X', '--expand', action="store_true", default=False)
    parser.add_argument('-tb', '--table', type=str)
    parser.add_argument('-db', '--database', type=str)
    parser.add_argument('-a', '--elements')
    parser.add_argument('-f', '--find')
    args = parser.parse_args()

    if args.info:
        if args.virtualmachine:
            vm = args.virtualmachine
            if args.database:
                db = args.database
                if args.table:
                    table = args.table
                    pretty_info(instance=vm, db=db, table=table, expand=args.expand)
                    return
                pretty_info(instance=vm, db=db, expand=args.expand)
                return
            pretty_info(instance=vm, expand=args.expand)
            return

    if parser.find:
        pass

    if parser.add:
        pass


_SHOW_DATA_BASES = "SHOW DATABASES;"
_CREATE_DATA_BASE = "CREATE DATABASE {0};"
_DELETE_DATA_BASE = "DROP DATABASE {0};"
_USE_DATA_BASE = "USE {0};"
_SHOW_TABLE = "DESC {0};"
_SHOW_ALL_TABLES = "show tables;"
_CREATE_TABLE = "CREATE TABLE {0} ({1});"
_DELETE_TABLE = "DROP TABLE {0};"
_ADD_COLUMN = """
    ALTER TABLE {0}
    ADD {1} {2};"""
_DELETE_COLUMN = """
    ALTER TABLE {0}
    DROP COLUMN {1};"""
_CHANGE_COLUMN = """
    ALTER TABLE {0}
    CHANGE {1} {2} {3};"""
_ADD_VALUE = "I" + "NSERT INTO {0} VALUES {1};"
_SHOW_TABLE_VALUES = "S" + "ELECT * FROM {0};"
_FIND_VALUES_TABLE = ""
_INSERT_VALUE = ""
_WHERE_STM = ""


_protocol_noprotocol = ' VARCHAR(10) NOT NULL,'
_protocol_taxon = {'s' : ' VARCHAR(10) NOT NULL,',
                   'i' : ' INT NOT NULL,',
                   'p' : ' PRIMARY KEY {0} '}


def _query_create_table(name, fields):
    _funquery = ''
    for field in fields:
        if ':' in field:
            field1, code = field.split(':')
            _funquery += ' ' + field1
            for c in code:
                if c == 'p':
                    _funquery += (_protocol_taxon['p']).format(field1)
                    continue
                _funquery += _protocol_taxon[c]
            continue
        _funquery += ' ' + field + _protocol_noprotocol
    _query = _CREATE_TABLE.format(name, _funquery)
    return _query[0:-3] + _query[-2:]

def execute_sql_query(instance=None, sql=None, rs=False):
    if instance is None:
        connect = mysql_connect(local=True)
    connect = mysql_connect(instance=instance)
    res = None
    with connect.cursor() as cursor:
        if type(sql) == list:
            for query in sql:
                cursor.execute(query)
        else:
            cursor.execute(sql)
        if rs:
            res = cursor.fetchall()
            return res

@_firstraws
def instance_databases(instance=None):
    return execute_sql_query(instance=instance, sql=_SHOW_DATA_BASES, rs=True)


@_firstraws
def instance_tables(instance=None, db=None):
    if db:
        if db == 'ALL':
            return instance_tables(instance=instance, db=None)
        return execute_sql_query(instance=instance,
                                 sql=[_USE_DATA_BASE.format(db), _SHOW_ALL_TABLES],
                                 rs=True)
    else:
        databases = instance_databases(instance=instance)
        return [instance_tables(instance=instance, db=d) for d in databases]


def instance_create_db(instance=None, db=None):
    if db is None:
        err = ('db is None')
        raise NameError(err)

    if db in instance_databases(instance=instance):
        err = ('db exist already')
        raise Exception(err)

    execute_sql_query(instance=instance,
                      sql=_CREATE_DATA_BASE.format(db),
                      rs=False)


def instance_delete_db(instance=None, db=None):
    if db is None:
        err = ('db is None')
        raise NameError(err)

    if not db in instance_databases(instance=instance):
        err = ('db doesnt exist')
        raise Exception(err)

    execute_sql_query(instance=instance,
                      sql=_DELETE_DATA_BASE.format(db),
                      rs=False)


def instance_exit_db(instance=None, db=None):
    if db is None:
        err = ('db is None')
        raise NameError(err)
    if not db in instance_databases(instance=instance):
        return False
    return True


def instance_select_db(instance=None, db=None):
    if db is None:
        err = ('db is None')
        raise NameError(err)

    if not instance_exit_db(instance=instance, db=db):
        err = ('Database not found')
        raise NameError(err)

    execute_sql_query(instance=instance, sql=ATA_BASE.format(db), rs=False)


def database_tables(instance=None, db=None):
    if db is None:
        err = ('db is None')
        raise NameError(err)

    return instance_tables(instance=instance, db=db)

@_firstraws
def table_fields(instance=None, db=None, table=None):
    if db is None or table is None:
        err = ('db or table is None')
        raise NameError(err)

    return execute_sql_query(instance=instance,
                             sql=[_USE_DATA_BASE.format(db),
                                  _SHOW_TABLE.format(table)],
                             rs=True)


def create_table(instance=None, db=None, table=None, fields=['id']):
    if db is None or table is None:
        err = ('db or table is None')
        raise NameError(err)

    if not instance_exit_db(instance=instance, db=db):
        err = ('db doesnt exist')
        raise NameError(err)

    if database_exist_table(instance=instance,
                           db=db,
                           table=table):
        err = ('table exist already')
        raise NameError(err)

    execute_sql_query(instance=instance,
                      sql=[ATA_BASE.format(db),
                           _query_create_table(table, fields)],
                      rs=False)

def table_values(instance=None, db=None, table=None):
    if db is None or table is None:
        err = ('db or table is None')
        raise NameError(err)

    if not instance_exit_db(instance=instance, db=db):
        err = ('db doesnt exist')
        raise NameError(err)

    if not database_exist_table(instance=instance,
                               db=db,
                               table=table):
        err = ('table doesnt exist')
        raise NameError(err)

    return execute_sql_query(instance=instance,
                             sql=[ATA_BASE.format(db),
                                  _SHOW_TABLE_VALUES.format(table)],
                             rs=True)

def delete_table(instance=None, db=None, table=None):
    if db is None or table is None:
        err = ('db or table is None')
        raise NameError(err)

    if not instance_exit_db(instance=instance, db=db):
        err = ('db doesnt exist')
        raise NameError(err)

    if not database_exist_table(instance=instance,
                               db=db,
                               table=table):
        err = ('table doesnt exist')
        raise NameError(err)

    execute_sql_query(instance=instance,
                      sql=[ATA_BASE.format(db),
                           _DELETE_TABLE.format(table)],
                      rs=False)


def add_field():
    pass

def del_field():
    pass

def change_field():
    pass


def add_value(instance=None, db=None, table=None, value=None):
    if db is None or table is None:
        err = ('db or table is None')
        raise NameError(err)

    if not instance_exit_db(instance=instance, db=db):
        err = ('db doesnt exist')
        raise NameError(err)

    if not database_exist_table(instance=instance,
                               db=db,
                               table=table):
        err = ('table doesnt exist')
        raise NameError(err)

    if value is None:
        return
    else:
        value=tuple(value)

    execute_sql_query(instance=instance,
                      sql=[ATA_BASE.format(db),
                           _ADD_VALUE.format(table, values)],
                      rs=False)

def get_architecture(instance=None):
    res = {}
    tb = None
    db = instance_databases(instance=instance)
    for database in db:
        for table in database_tables(instance=instance, db=database):
            res[database][table] = table_fields(instance=instance,
                                                db=db,
                                                table=table)
    return res

def adjust_db_architecture(instance=None):
    pass

def assert_architecture(instance=None):
    Arc1 = get_architecture(instance=instance)
    Arc2 = get_db_architecture(instance=instance)
    missing_db = []
    missing_tb = []
    missing_fd = []

    def compare_tb(a, b):
        def compare_db(a, b):
            lb = (list.b.keys())
            for k in list(a.keys()):
                if not k in lb:
                    missing_db.append(k)
                else:
                    match_db += [k]
            return missing_db, match_db
        x, y = compare_db(a, b)
        for db in y:
            w, z = compare_db(a[db], b[db])
            if w:
                missing_tb += [(db, w)]
                continue
            else:
                for uw in z:
                    for f in table_fields(instance=instance,
                                          db=db,
                                          table=uw):
                        if f in a[uw][f]:
                            continue
                        missing_fd += [f]
    compare_tb(a, b)
    if not missing_db:
        return True
    if not missing_fd:
        if not missing_tb:
            return (missing_db,)
        return missing_db, missing_tb
    return missing_db, missing_tb, missing_fd

def build_instance_architecure(instance=None, ecrase=False):
    if _equal_list(assert_architecture(instance=instance),
                   list(get_architecture(instance=instance).keys())) or ecrase:
        build_architecture(instance=instance)

def build_architecture(instance=None):
    Arc = get_db_architecture(instance=instance)
    for db in list(Arc.keys()):
        instance_create_db(db)
        for table, fields in Arc[db].items():
            create_table(instance=instance,
                         db=db,
                         table=table,
                         fields=fields)


def cleanup_architecture(instance=None):
    Arc = get_db_architecture(instance=instance)
    _db = instance_databases(instance=instance)
    for db in list(Arc.keys()):
        if db in _db:
            instance_delete_db(instance=instance, db=db)

def rebuild_architecture(instance=None):
    cleanup_architecture(instance=instance)
    build_architecture(instance=instance)


def instance_stats(instance=None):
    pass

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



def find_in_table(instance=None,
                  db=None,
                  table=None,
                  **kwargs):
    if not (table and db):
        err = ('Targets error')
        raise NameError(err)

    matches = []
    keys = list(kwargs.keys())
    if not _include_list(keys,
                         table_fields(instance=instance,
                                      db=db),
                                      table=table):
        err = ('kwargs matching error')
        raise Exception(err)

    execute_sql_query(instance=instance,
                      sql=[ATA_BASE.format(db),
                           _FIND_VALUES_TABLE.format(table,
                                                     _WHERE_STM(kwargs))])

def find_matches(instance=None, db=None, target_fields=None, targets=None):
    pass

def find(instance=None, db=None, table=None, target_fields=None, targets=None):
    pass

def jsonise_table(instance=None, db=None, table=None, file=None):
    pass

def josenise_database(instance=None, db=None, table=None, file=None):
    pass



if __name__ == "__main__":
    main()
