from greww.data.mysql import (_version,
                              _user,
                              databases,
                              make_database,
                              remove_database,
                              use_database,
                              tables,
                              table_fields,
                              table_fields_data,
                              table_primary_start,
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

db = "greww_mysql_tests_0"
tb = "test_table"

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

def test_mysql_version():
    assert _version() >= '5.7'
    assert _user()
    # coverage tests
    use_database('kikou')
    copy_table('', '', '')
    return 1

def test_mysql_database_manipulations():
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


def test_mysql_tables_manipulations():
    global db, tb
    # init
    make_database(db)
    _tb = tables(db)
    # make table
    assert len(_tb) == 0
    make_table(db,
               tb,
               field1="INT(2)",
               field2="VARCHAR(3)",
               field3="JSON")
    _tb = tables(db)
    assert tb in _tb
    # check fields
    fields = table_fields(db, tb)
    assert "field1" in fields and \
           "field2" in fields and \
           "field3" in fields
    fields_data = table_fields_data(db, tb)
    # check fields type
    assert len(fields_data) == 3
    assert fields_data[0][0] == "field1"
    assert fields_data[0][1] == "int(2)"
    assert fields_data[1][0] == "field2"
    assert fields_data[1][1] == "varchar(3)"
    assert fields_data[2][0] == "field3"
    assert fields_data[2][1] == "json"
    # check fields manipulations
    add_field(db, tb, "field4", "BOOLEAN")
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 4
    assert fields_data[3][0] == "field4"
    assert fields_data[3][1] == "tinyint(1)"
    # change field
    change_field(db, tb, "field4", "fieldc", "INT(5)")
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 4
    assert fields_data[3][0] == "fieldc"
    assert fields_data[3][1] == "int(5)"
    # delete field
    remove_field(db, tb, "fieldc")
    fields_data = table_fields_data(db, tb)
    assert len(fields_data) == 3
    # assert ??
    # clean table
    remove_table(db, tb)
    _tb = tables(db)
    assert len(_tb) == 0
    # Clean up test database
    remove_database(db)
    return 1

test_mysql_tables_manipulations()

def test_mysql_tables_content_basic_manipulations():
    # init
    make_database(db)
    _tb = tables(db)
    make_table(db,
               tb,
               field1="INT(2)",
               field2="VARCHAR(3)",
               field3="JSON",
               primary_key="field1")
    table_primary_start(db, tb, 0)
    # table content
    ct = table_content(db, tb)
    assert len(ct) == 0
    # add elements
    add_element(db, tb, field2="kik")
    add_element(db, tb, field2="kok", field3='[]')
    ct = table_content(db, tb)
    assert len(ct) == 2
    assert ct[0][0] == 0
    assert ct[0][1] == "kik"
    assert ct[0][2] is None
    assert ct[1][0] == 1
    assert ct[1][1] == "kok"
    assert ct[1][2] == '[]'
    # remove element
    remove_elements(db, tb, where="field2 = 'kik'")
    # recheck ct
    ct = table_content(db, tb)
    assert len(ct) == 1
    assert ct[0][1] == "kok"
    assert ct[0][2] == '[]'
    remove_elements(db, tb, where="field3 = '[]'", with_limit=1)
    ct = table_content(db, tb)
    assert len(ct) == 0
    # clean
    remove_table(db, tb)
    remove_database(db)
    return 1

def _column_of_matrix(matrix, column):
    return [i[column] for i in matrix]

def test_mysql_tables_content_selection():
    #init
    make_database(db)
    _tb = tables(db)
    make_table(db,
               tb,
               field1="INT(3) NOT NULL AUTO_INCREMENT",
               field2="VARCHAR(3)",
               field3="JSON",
               primary_key="field1")
    table_primary_start(db, tb, 0)
    add_element(db, tb, field2="kik", field3="[]")
    add_element(db, tb, field2="kok", field3='[0]')
    add_element(db, tb, field2="daw", field3='[]')
    add_element(db, tb, field2="rek", field3='[2, 3]')
    #select
    selection = select_elements(db,
                                tb,
                                with_limit=1,
                                selection='field2',
                                where="field1 = 3")
    assert len(selection) == 1
    assert selection[0][0] == 'daw'
    selection = select_elements(db,
                                tb,
                                selection='field2 , field3',
                                where="field1 > 2")
    assert len(selection) == 2
    assert selection[0][0] == 'daw'
    assert selection[0][1] == '[]'
    assert selection[1][0] == 'rek'
    assert selection[1][1] == '[2, 3]'
    selection = select_optimised(db,
                                 tb,
                                 with_limit=2,
                                 selection="*",
                                 kind="ASC",
                                 sorted_by="field1")
    assert _column_of_matrix(selection, 0) == [1, 2]

def test_mysql_tables_content_update():
    pass


__all__ = [test_connectors,
           test_connection_cursors,
           test_mysql_version,
           test_mysql_database_manipulations,
           test_mysql_tables_manipulations,
           test_mysql_tables_content_basic_manipulations,
           test_mysql_tables_content_selection,
           test_mysql_tables_content_update]
