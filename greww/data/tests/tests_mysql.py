from greww.data.mysql import (databases,
                              make_database,
                              remove_database,
                              use_database,
                              tables,
                              table_fields,
                              table_content,
                              make_table,
                              remove_table,
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
                              ConnectorsGenerator)

_connectors = ConnectorsGenerator()
#_connectors._new()
M = MysqlPen()

db = "zilean_tests_0"
table = "test_table"

def test_connectors():
    assert _connectors
    cnx = _connectors.gen
    assert cnx
    _connectors._reset()
    cnx = _connectors.gen
    assert cnx
    return 1

def test_connection_cursors():
    cursor = _connectors.gen.cursor()
    cursor.execute("SHOW DATABASES")
    _databases = [i for i in cursor]
    assert len(_databases) >= 4
    return 1

test_connection_cursors()

def test_mysql_database_manipulation():
    db = databases()
    assert db
    assert len(db) >= 4
    assert "sys" in db
    make_database("db")
    db = databases()
    assert "db" in db
    remove_database("db")
    db = databases()
    assert not "db" in db
    return 1

def test_mysql_tables_manipulation():
    make_database("db")
    make_table("db",
               "test_table",
               field1="INT(2)",
               field2="VARCHAR(3)",
               field3="JSON")
    fields = table_fields()
    remove_table("zilean_test_0", "test_table")
    return 1

__all__ = [test_connectors,
           test_connection_cursors,
           test_mysql_database_manipulation,
           test_mysql_tables_manipulation]
