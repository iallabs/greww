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
tb = "test_table"

def test_connectors():
    assert _connectors
    cnx = _connectors.gen
    assert cnx
    _connectors._reset()
    cnx = _connectors.gen
    assert cnx
    return 1

#test_connectors()

def test_connection_cursors():
    cursor = _connectors.gen.cursor()
    cursor.execute("SHOW DATABASES")
    _databases = [i for i in cursor]
    assert len(_databases) >= 4
    return 1

#test_connection_cursors()

def test_mysql_database_manipulation():
    global db, tb
    _db = databases()
    assert _db
    assert len(_db) >= 4
    assert "mysql" in _db
    make_database(db)
    _db = databases()
    assert db in _db
    remove_database(db)
    _db = databases()
    assert not (db in _db)
    return 1

print("XXXXXXXXXXXXXXXXXXXX")
test_mysql_database_manipulation()
print("XXXXXXXXXXXXXXXXXXXX")

def test_mysql_tables_manipulation():
    global db, tb
    make_database(db)
    _tb = tables(db)
    assert len(_tb) == 0
    make_table(db,
               tb,
               field1="INT(2)",
               field2="VARCHAR(3)",
               field3="JSON")
    _tb = tables(db)
    assert tb in _tb
    fields = table_fields(db, tb)
    assert "field1" in fields and \
           "field2" in fields and \
           "field3" in fields
    remove_table(db, tb)
    _tb = tables(db)
    assert len(_tb) == 0
    # Clean up test database
    remove_database(db)
    return 1

print("XXXXXXXXXXXXXXXXXXXX")
test_mysql_tables_manipulation()
print("XXXXXXXXXXXXXXXXXXXX")

__all__ = [test_connectors,
           test_connection_cursors,
           test_mysql_database_manipulation,
           test_mysql_tables_manipulation]
