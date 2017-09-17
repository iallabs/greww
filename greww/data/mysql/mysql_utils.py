from .mysql_access import (execute_only,
                           execute_and_fetch)

from greww.utils.filters import refetch_filter

from .mysql_query import (_VERSION,
                          _USER,
                          _USE_DATABASE,
                          _SHOW_DATABASES,
                          _CREATE_DATABASE,
                          _DELETE_DATABASE,
                          _SHOW_TABLES,
                          _TABLE_FIELDS,
                          _CREATE_TABLE,
                          _SELECT_TABLE,
                          _USE_DATABASE,
                          _DELETE_TABLE,
                          _IE_QUERY,
                          _DL_QUERY,
                          _SL_QUERY,
                          _CT_QUERY,
                          _UE_QUERY,
                          _AUTOINCR,
                          _ADD_COLUMN,
                          _DELETE_COLUMN,
                          _CHANGE_COLUMN,
                          _SELECT_OPTI)

def _version():
    """
    """
    return execute_and_fetch(_VERSION)[0][0]

def _user():
    """
    """
    return execute_and_fetch(_USER)[0][0]


@refetch_filter([0])
def databases():
    """
    return a list of strings containing msql databases
    =======================================================
    >>> from greww.data.mysql import databases
    >>> databases()
    ["sys", "mysql"]
    =======================================================
    """
    return execute_and_fetch(_SHOW_DATABASES)

def make_database(dbname):
    """
    make a mysql database
    =======================================================
    >>> from greww.data.mysql import make_database, databases
    >>> make_database('kikou')
    >>> databases()
    ["sys", "mysql", "kikou"]
    =======================================================
    """
    execute_only(_CREATE_DATABASE.format(dbname))

def remove_database(dbname):
    """
    Remove a mysql database
    =======================================================
    >>> from greww.data.mysql import (remove_database,
                                      databases)
    >>> remove_database('kikou')
    >>> databases()
    """
    execute_only(_DELETE_DATABASE.format(dbname))

def use_database(dbname): #XXX: Maybe is useless
    """
    Use mysql databases
    execute_only(_USE_DATABASE.format(dbname))
    """
    pass

@refetch_filter([0])
def tables(dbname):
    """
    return a list of strings containing mysql tables at one
    given database
    =======================================================
    >>> from greww.data.mysql import tables
    >>> tables("sys")
    ["host_ip", "host_kappa" ... ""]
    =======================================================
    """
    return execute_and_fetch(_SHOW_TABLES.format(dbname))

@refetch_filter([0])
def table_fields(dbname, table):
    """
    Return a list of table fields ( only their names )
    =======================================================
    """
    return execute_and_fetch(_TABLE_FIELDS.format(dbname, table))

def table_fields_data(dbname, table):
    """
    Return a list of table fields ( All data )
    =======================================================
    """
    return execute_and_fetch(_TABLE_FIELDS.format(dbname, table))

def add_field(db, table, field_name, field_type):
    """
    Add field to table at db
    =======================================================
    """
    execute_only(_ADD_COLUMN.format(db, table, field_name, field_type))

def remove_field(db, table, field_name):
    """
    Remove field from table at db
    =======================================================
    """
    execute_only(_DELETE_COLUMN.format(db, table, field_name))

def change_field(db, table, field_name, new_field, field_type):
    """
    Change field in table at db
    =======================================================
    """
    execute_only(_CHANGE_COLUMN.format(db,
                                       table,
                                       field_name,
                                       new_field,
                                       field_type))


def make_table(db, table, **kwargs):
    """
    Create a table at database with kwargs as fields
    =======================================================
    >>> from greww.data.mysql import make_table
    >>> make_table("db1", "tb1", id="INT(5)", name="VARCHAR(10)")
    """
    execute_only(_CT_QUERY(db, table, **kwargs))

def remove_table(db, table):
    """
    Drop table at db
    =======================================================
    """
    return execute_only(_DELETE_TABLE.format(db, table))

def table_content(db, table):
    """
    return a 2 dimentioanl array cont-aining all table values
    ========================================================
    >>> table_content("sys", "host_ip")
    [[1, 2, 3],
     [2, 3, 4],
     [3, 4, 5]]
    ========================================================
    """
    #XXX: uses : `select * from table`
    return execute_and_fetch(_SELECT_TABLE.format(db, table))

def table_primary_start(db, table, start):
    """
    Set table starting point for AUTO_INCREMENT PRIMARY Key
    """
    return execute_only(_AUTOINCR.format(db, table, start))

def copy_table(db, table, target_table):
    """
    Not Implemented
    =======================================================
    """
    pass

def add_element(db, table, **kwargs):
    """
    add element to table at db
    =======================================================
    """
    return execute_only(_IE_QUERY(db, table, **kwargs), commit=True)

def remove_elements(db, table, with_limit=-1, where=None):
    """
    Remove Element from table at db
    =======================================================
    """
    return execute_only(_DL_QUERY(db, table, where, with_limit), commit=True)

def select_elements(db, table, with_limit=-1, selection=None, where=None):
    """
    Select elements that satisfy kwargs from table at db
    =======================================================
    """
    return execute_and_fetch(_SL_QUERY(db, table, where, with_limit, selection))

def update_element(db, table, with_limit=-1, sets=None, where=None):
    """
    """
    return execute_only(_UE_QUERY(db, table, where, with_limit, sets), commit=True)

def select_optimised(db,
                     table,
                     with_limit=1,
                     selection="*",
                     kind="ASC",
                     sorted_by=None):
    """
    Select optimised
    =======================================================
    """
    return execute_and_fetch(_SELECT_OPTI.format(selection,
                                                 db,
                                                 table,
                                                 sorted_by,
                                                 kind,
                                                 with_limit))

MysqlApiFunctions = {"_version" : _user,
                     "_user" : _user,
                     "databases" : databases,
                     "make_database" : make_database,
                     "remove_database" : remove_database,
                     "use_database" : use_database,
                     "tables" : tables,
                     "table_fields" : table_fields,
                     "table_content" : table_content,
                     "make_table" : make_table,
                     "remove_table" : remove_table,
                     "copy_table" : copy_table,
                     "add_field" : add_field,
                     "remove_field" : remove_field,
                     "change_field" : change_field,
                     "add_element" : add_element,
                     "remove_elements" : remove_elements,
                     "select_elements" : select_elements,
                     "update_element" : update_element,
                     "select_optimised" : select_optimised}
