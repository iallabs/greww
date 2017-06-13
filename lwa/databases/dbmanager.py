# this is databases connector to python

import pymysql.cursors
from lwa.utils.decorators import _firstraws, _validpd, _forall
from lwa.utils.functions import _certify, _include_list, _equal_list, _compare_l1

class _ConnectionFailled(Exception):
    pass

class _NotAuthorisedMethod(Exception):
    pass

class _IncompatibleDataUnit(Exception):
    pass

class _NotAuthorisedOperation(Exception):
    pass

databases = ['testdb']

_SHOW_DATA_BASES = "SHOW DATABASES;"
_CREATE_DATA_BASE = "CREATE DATABASE {0};"
_DELETE_DATA_BASE = "DROP DATABASE {0};"
_USE_DATA_BASE = "USE {0};"
_SHOW_TABLE = "DESC {0};"
_SHOW_ALL_TABLES = "show tables;"
_CREATE_TABLE = "CREATE TABLE {0} ({1});"
_DELETE_TABLE = "DROP TABLE {0};"
_ADD_COLUMN = "A" + "LTER TABLE" + " {0} " + "ADD" + " {1} " + "{0};"
_DELETE_COLUMN = "ALTER TABLE {0} DROP COLUMN {1};"
_CHANGE_COLUMN = "ALTER TABLE {0} CHANGE {1} {2} {3};"
_ADD_VALUE = "I" + "NSERT INTO {0} VALUES {1};"
_SHOW_TABLE_VALUES = "S" + "ELECT * FROM {0};"
_INSERT_VALUE = ""

_protocol_noprotocol = ' VARCHAR(10) NOT NULL,'
_protocol_taxon = {'s' : ' VARCHAR(10) NOT NULL,',
                   'i' : ' INT NOT NULL,',
                   'p' : ' PRIMARY KEY {0} '}


def _connect_mysql(host, user, pw):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=pw)
    return connection

def _connect_withdb(host, user, pw , db):
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=pw,
                                 db=db)
    return connection


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



class DBManager:
    # Mysql database manager

    __slots__ = ['connection', 'state', 'db']

    def __init__(self, connection=None, connection_args=()):
        if connection_args:
            host, user, pw, db = connection_args
            if db:
                try:
                    self.connection = _connect_withdb(host, user, pw, db)
                    self.state = 2
                    self.db = [db]
                    print("Connected to mysql successfully.")
                    print("Connected to database : ", db)
                except:
                    raise _ConnectionFailled('Failed to connect *i1')
            else:
                try:
                    self.connection = _connect_mysql(host, user, pw)
                    self.state = 1
                    self.db = databases
                    print("Connected to mysql successfully.")
                except:
                    raise _ConnectionFailled('Failed to connect *i2')
        elif connection:
            self.connection = connection
            print('Connected to connection_obj', connection)
            self.state = -1
            self.db = databases

    def _execute(self, sql, rs=True):
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            if rs:
                result = cursor.fetchall()
                return result

    @property
    @_firstraws
    def _databases(self):
        return self._execute(_SHOW_DATA_BASES, rs=True)

    @property
    @_firstraws
    def _dbtables(self):
        if self.state == 1:
            raise _NotAuthorisedMethod('Select a database ')
        return self._execute(_SHOW_ALL_TABLES, rs=True)

    def create_database(self, dbname):
        sql = _CREATE_DATA_BASE.format(dbname)
        self._execute(sql, rs=False)
        print('Created database : ', dbname)

    def delete_database(self, dbname):
        if not dbname in self._databases:
            print('no database named', dbname)
            return
        sql = _DELETE_DATA_BASE.format(dbname)
        self._execute(sql, rs=False)
        print('Deleted database : ', dbname)

    def use_database(self, dbname, show=False):
        if not dbname in self._databases:
            print('no database named', dbname)
            return
        sql = _USE_DATA_BASE.format(dbname)
        self._execute(sql, rs=False)
        self.state = 2
        if show: print('Selected database : ', dbname)

    @_firstraws
    def _table_columns(self, table=None, db=None, show=False):
        if self.state == 1 and db is None:
            raise _NotAuthorisedMethod('Please select a database first')
        if db:
            self.use_database(db)
        if not table in self._dbtables:
            if show: print(table, '  doesnt exist in database tables')
            return
        sql = _SHOW_TABLE.format(table)
        return self._execute(sql, rs=True)


    def _create_table(self, db=None, table=None, columns=None, show=False):
        if self.state == 1 and db is None:
            raise _NotAuthorisedMethod('Please select a database first')
        try:
            sql = _query_create_table(table, columns)
            self._execute(sql, rs=False)
            if show: print('Created table : ', table , 'with fields', columns)
        except:
            raise _NotAuthorisedOperation('Cant create table ', table)

    def _show_table(self, db=None, table=None, show=False):
        if self.state == 1 and db is None:
            raise _NotAuthorisedMethod('Please select a database first')
        if db:
            self.use_database(db)
        if not table in self._dbtables:
            if show: print(table, '  doesnt exist in database tables')
            return
        try:
            sql = _SHOW_TABLE_VALUES.format(table)
            return self._execute(sql, rs=False)
        except:
            raise _NotAuthorisedOperation('Cant show table ', table)

    def _delete_table(self, db=None, table=None, show=False):
        if self.state == 1 and db is None:
            raise _NotAuthorisedMethod('Please select a database first')
        if db:
            self.use_database(db)
        if not table in self._dbtables:
            if show: print(table, '  doesnt exist in database tables')
            return
        try:
            sql = _DELETE_TABLE.format(table)
            self._execute(sql)
            if show: print('Deleted table : ', table)
        except:
            raise _NotAuthorisedOperation('Cant delete table ', table)

    def _add_columns(self, db=None, table=None, column=None, typ='VARCHAR(10)', show=False):
        if self.state == 1 and db is None:
            raise _NotAuthorisedMethod('Please select a database first')
        if db:
            self.use_database(db)
        if not table in self._dbtables:
            if show: print(table, '  doesnt exist in database tables')
            return
        with self.connection.cursor() as cursor:
            sql = _ADD_COLUMN.format(table, column, typ)
            cursor.execute(sql)
            if show: print('Added Field : ', table)

    def _del_column(self, tablename, collumn, show=False):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        if not tablename in self._dbtables:
            if show: print(tablename, '  doesnt exist in database tables')
            return
        with self.connection.cursor() as cursor:
            sql = _DELETE_COLUMN.format(tablename, column)
            cursor.execute(sql)
            if show: print('Deleted Field : ', tablename)

    def _change_column(self, tablename, column , new_column, new_type, show=False):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        if not tablename in self._dbtables:
            if show: print(tablename, '  doesnt exist in database tables')
            return
        sql = _CHANGE_COLUMN.format(tablename, column, new_column, new_type)
        self._execute(sql)
        if show: print('Change Field in ', tablename, ' : ', column ,' --> ', new_column)

    def _add_value(self, dataunit=None, table=None, show=True):
        if dataunit is None:
            return
        if dataunit.db is None:
            print('Select a database or set dataunit db')
            return
        db = dataunit.db
        table = dataunit.table or table
        if self.state == 1:
            self.use_database(db)
        if table is None:
            print('Select a table')
            return
        if not table in self._dbtables:
            if show: print(table, '  doesnt exist in database tables')
            return
        if _include_list(dataunit.keys, self._table_columns(table)):
            with self.connection.cursor() as cursor:
                sql = _ADD_VALUE.format(table, dataunit.quantify)
                cursor.execute(sql)
                print('added value')

        else:
            raise _IncompatibleDataUnit('Not compatible data unit')

    def _insert_value(self, dataunit, aid=None, aname=None, db=None, table=None):
        pass
