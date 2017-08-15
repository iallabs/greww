from greww.data.mysql import (databases,
                              make_database,
                              remove_database,
                              use_database,
                              tables,
                              table_fields,
                              table_content,
                              make_table,
                              remove_table,
                              talbe_primary_start,
                              copy_table,
                              add_field,
                              remove_field,
                              change_field,
                              add_element,
                              remove_elements,
                              select_elements,
                              update_element,
                              select_optimised,
                              MysqlPen,

from greww.data.mysql.mysql_access import ConnectorsGenetor

_connectors = ConnectorsGenetor()
M = MysqlPen()


def test_connectors():
    assert _connectors:
    cnx = _connectors.gen
    assert cnx
    _connectors._reset()
    cnx = _connectors.gen
    assert cnx

def test_connection_cursors():
    cursor = _connectors.gen.cursor()
    cursor.execute("SHOW DATABASES")
    _databases = [i for i in cursor]
    assert _databases != []
    assert len(_databases) > 4

def test_mysql_database_manipulation():
    db = databases()
