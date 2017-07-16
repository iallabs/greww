from greww.settings import SETTINGS
from greww.data.mysql.mysql_utils import (mysql_connect,
                                          get_instance_sql,
                                          execute_sql_query,
                                          instance_databases,
                                          instance_tables,
                                          instance_create_db,
                                          instance_delete_db,
                                          instance_exist_db,
                                          database_exist_table,
                                          table_fields,
                                          _query_create_table,
                                          create_table,
                                          table_values,
                                          delete_table,
                                          add_value_wk,
                                          get_architecture,
                                          adjust_db_architecture,
                                          assert_architecture,
                                          build_instance_architecture,
                                          build_architecture,
                                          cleanup_architecture,
                                          rebuild_architecture,
                                          find_in_table,
                                          select_from_table)

_SHOW_DATA_BASES = "SHOW DATABASES;"
_SHOW_ALL_TABLES = "show tables;"

db_a = "sys"
dbgreww = "grewwdb"
tbgreww = "grewwmysqltests"
dbtbgreww = "grewwdb.grewwmysqltests"

_settings = SETTINGS("mysql_utils", "ALL")

path = _settings["WORKING_DIRECTORY"]

MYSQL_LOGS = _settings["MYSQL_LOGS"]

if MYSQL_LOGS["Active"]:
    pytests = ['mysql_connect',
               'objective_tests',
               'mysql_db_tests',
               'mysql_table_tests',
               'mysql_insert_tests',
               'mysql_insert_tests']
    mlogs = MYSQL_LOGS["Logs"]
else:
    pytests = []

ctests = []


print(mlogs)

def mysql_connect():
    a = mysql_connect(mlogs=mlogs)
    assert not (a is None)

def objective_tests():
    #TODO: get_instance_sql
    #TODO: _query_create_table
    x = execute_sql_query(sql=_SHOW_DATA_BASES,
                          rs=True,
                          commit=False)
    assert not (x is None)
    y = execute_sql_query(sql=[_USE_DATA_BASES.format(db_a),
                               _SHOW_ALL_TABLES],
                          rs=True,
                          commit=False)
    assert not (y is None)


def mysql_db_tests():
    a = instance_databases()
    assert not (a is None)
    assert not (dbgreww in a)
    instance_create_db(db=dbgreww)
    a = instance_databases()
    assert dbgreww in a
    instance_delete_db(db=dbgreww)
    a = instance_databases()
    assert not (dbgreww in a)
    instance_create_db(db=dbgreww)
    create_table(db=dbgreww,
                 table=tbgreww,
                 fields=["test", "id", "date"])
    assert database_exist_table(db=dbgreww, table=tbgreww)
    instance_delete_db(db=dbgreww)

def mysql_table_tests():
    instance_create_db(db=dbgreww)
    create_table(db=dbgreww,
                 table=tbgreww,
                 fields=["test", "p:id", "u:id2", "I:nothing"])
    fields = table_fields(db=db, table=table)
    assert "test" in fields\
           and "id" in fields\
           and "id2" in fields\
           and "nothing" in fields
    delete_table(db=dbgreww, table=tbgreww)
    a = instance_tables(db=dbgreww)
    b = instance_databases()
    assert not tbgreww in a
    assert dbgreww in b
    instance_delete_db(db=dbgreww)

def mysql_insert_tests():
    pass


def mysql_select_tests():
    pass

mysql_db_tests()
objective_tests()
mysql_table_tests()
mysql_insert_tests()

