# this is databases connector to python

import pymysql.cursors

databases = ['testdb']

class _ConnectionFailled(Exception):
    pass

class _NotAuthorisedMethod(Exception):
    pass

class _IncompatibleDataUnit(Exception):
    pass

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

_SHOW_DATA_BASES = "SHOW DATABASES;"
_CREATE_DATA_BASE = "CREATE DATABASE {0};"
_DELETE_DATA_BASE = "DROP DATABASE {0};"
_USE_DATA_BASE = "USE {0};"
_SHOW_TABLE = "DESC {0};"
_SHOW_ALL_TABLES = "show tables;"
_CREATE_TABLE = "CREATE TABLE {0} ({1});"
_DELETE_TABLE = "DROP TABLE {0};"
_ADD_COLUMN = "ALTER TABLE {0} ADD COLUMN {1} {0};"
_DELETE_COLUMN = "ALTER TABLE {0} DROP COLUMN {1};"
_CHANGE_COLUMN = "ALTER TABLE {0} CHANGE {1} {2} {3};"
_ADD_VALUE = "I" + "NSERT INTO {0} VALUES ({1});"
_SHOW_TABLE_VALUES = "S" + "ELECT * FROM {0};"
_INSERT_VALUE = ""

_protocol_noprotocol = ' VARCHAR(10) NOT NULL,'
_protocol_taxon = {'s' : ' VARCHAR(10) NOT NULL,',
                   'i' : ' INT NOT NULL,',
                   'p' : ' PRIMARY KEY {0} '}

def _include_list(ln, lp):
    if len(ln) > len(lp):
        return False
    for i in ln:
        if i in lp:
            continue
        return False
    return True

def _equal_list(ln, lp):
    return _include_list(ln, lp) and _include_list(lp, ln)

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


def _certify(d, _format):
    if not _format:
        return tuple(d.values())
    op = ()
    for field in _format:
        try:
            op += (d[field],)
        except:
            op += ('NULL',)
    return op


class DataUnit(object):
    # Data unit store a dict of fields and their contents
    # at _args
    table_format = []

    __slots__ = ['_args', '_db', '_table']

    def __init__(self, db=None, table=None, **kwargs):
        self._args = kwargs
        self._db = db
        self._table = table

    @property
    def args(self):
        return self._args

    @property
    def db(self):
        return self._db

    @property
    def table(self):
        return self._table

    @property
    def direct(self):
        return (self._db, self._table)

    @property
    def keys(self):
        return list(self.args.keys())

    @property
    def quantify(self):
        return _certify(self.args, self.table_format)

class TaxonDataUnit(DataUnit):
    table_format = ['name', 'type', 'level', 'pclass']
    pass

class SpeciesDataUnit(DataUnit):
    table_format = []
    pass


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

    @property
    def _databases(self):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *p3')
        with self.connection.cursor() as cursor:
            sql = _SHOW_DATA_BASES
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @property
    def _dbtables(self):
        if self.state == 1:
            raise _NotAuthorisedMethod('Connected to a database before using')
        with self.connection.cursor() as cursor:
            sql = _SHOW_ALL_TABLES
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


    def create_database(self, dbname):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *m4')
        with self.connection.cursor() as cursor:
            sql = _CREATE_DATA_BASE.format(dbname)
            cursor.execute(sql)
            print('Created database : ', dbname)

    def delete_database(self, dbname):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *m5')
        try:
            with self.connection.cursor() as cursor:
                sql = _DELETE_DATA_BASE.format(dbname)
                cursor.execute(sql)
                print('Deleted database : ', dbname)
        except:
            raise _NotAuthorisedMethod('Cant delete :', dbname)


    def use_database(self, dbname):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *m6')
        try:
            with self.connection.cursor() as cursor:
                sql = _USE_DATA_BASE.format(dbname)
                cursor.execute(sql)
                self.state = 2
                print('Selected database : ', dbname)
        except:
            raise _NotAuthorisedOperation('Cant select :', dbname)

    def _table_columns(self, table):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        with self.connection.cursor() as cursor:
            sql = _SHOW_TABLE.format(table)
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def _create_table(self, tablename, columns):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        try:
            with self.connection.cursor() as cursor:
                sql = _query_create_table(tablename, columns)
                cursor.execute(sql)
                print('Created table : ', tablename , 'with fields', columns)
        except:
            raise _NotAuthorisedOperation('Cant create table ', tablename)

    def _show_table(self, tablename):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        try:
            with self.connection.cursor() as cursor:
                sql = _SHOW_TABLE_VALUES.format(tablename)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except:
            raise _NotAuthorisedOperation('Cant show table ', tablename)

    def _delete_table(self, tablename):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        try:
            with self.connection.cursor() as cursor:
                sql = _DELETE_TABLE.format(tablename)
                cursor.execute(sql)
                print('Deleted table : ', tablename)
        except:
            raise _NotAuthorisedOperation('Cant delete table ', tablename)

    def _add_columns(self, tablename, column, typ):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        with self.connection.cursor() as cursor:
            sql = _ADD_FIELD.format(tablename, column, typ)
            cursor.execute(sql)
            print('Added Field : ', tablename)

    def _del_column(self, tablename, collumn):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        with self.connection.cursor() as cursor:
            sql = _DELETE_COLUMN.format(tablename, column)
            cursor.execute(sql)
            print('Deleted Field : ', tablename)

    def _change_column(self, tablename, column , new_column, new_type):
        if self.state == 1:
            raise _NotAuthorisedMethod('Please select a database first')
        with self.connection.cursor() as cursor:
            sql = _CHANGE_COLUMN.format(tablename, column, new_column, new_type)
            cursor.execute(sql)
            print('Change Field in ', tablename, ' : ', column ,' --> ', new_column)

    def _add_value(self, dataunit, table=None):
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
        if _include_list(dataunit.keys, self._table_columns(table)):
            with self.connection.cursor() as cursor:
                sql = _ADD_VALUE.format(table, dataunit.quantify)
                cursor.execute(sql)
                print('added value')

        else:
            raise _IncompatibleDataUnit('Not compatible data unit')

    def _insert_value(self, dataunit, aid=None, aname=None, db=None, table=None):
        pass


LICAPY_DATABASES = ['Plantae',
                    'Animalia',
                    'Fungi',
                    'Chromista',
                    'Virus',
                    'Bacteria',
                    'Essential Oils',
                    'Vegatal Oils']

LICAPY_SUPPORT_DATABASES = ['LicapyDB']

PLANTAE_DB = {'TreeData' : ('name', 'pname', 'level', 'bul'),
              'PlantsData' : ('name', 'name', 'pname', 'locations', 'carac')}

ANIMALIA_DB = {}
FUNGI_DB = {}
CHROMISTA_DB = {}
VIRUS_DB = {}
BACTERIA_DB = {}
ESSENTIAL_OILS_DB = {}
VEGETAL_OILS_DB = {}

LICAPY_DATABASES_EXPANDS = [PLANTAE_DB,
                            ANIMALIA_DB,
                            FUNGI_DB,
                            CHROMISTA_DB,
                            VIRUS_DB,
                            BACTERIA_DB,
                            ESSENTIAL_OILS_DB,
                            VEGETAL_OILS_DB]


def _compare_l1(ln, lp):
    for i in ln:
        if not i in lp:
            return False
    return True

class _NotAuthorisedOperation(Exception):
    pass

class LicapyDBManager(DBManager):
    # Licapy DataBase manager

    def __init__(self, cnxargs=(), db=LICAPY_DATABASES, sdb=LICAPY_SUPPORT_DATABASES):
        DBManager.__init__(connection=None, connection_args=cnxargs)
        if self.state == 2:
            raise _NotAuthorisedOperation('LicapyDBManager should connect to mysql')
        self.db = db + sdb
        if self._verify_db():
            print('Licapy databases are all created in mysql!')
        else:
            print('Not all Licapy databases are in mysql use ._build_db')

    def _verify_db(self):
        return _compare_l1(self.db, self._databases)

    def _build_db(self, ecrase=False):
        dbs = self._databases
        for database in self.db:
            if database in dbs:
                if ecrase:
                    self.delete_database(database)
                    self.create_database(database)
            else:
                self.create_database(database)

    def _verify_db_hierarchy(self, db):
        L = LICAPY_DATABASES
        architecture = LICAPY_DATABASES_EXPANDS[L.index(db)]
        if not architecture:
            print('No architecture given')
            return
        self.use_database(db)
        for table, content in architecture.items():
            if _compare_l1(content, self._table_columns(table)):
                return True
            return False

    def _build_db_architecture(self, db, ecrase=True):
        L = LICAPY_DATABASES
        architecture = LICAPY_DATABASES_EXPANDS[L.index(db)]
        if not architecture:
            print('No architecture given')
            return
        if not ecrase and self._verify_db_hierarchy(db):
            print('Database already built correctly')
            return
        self.use_database(db)
        for table, content in architecture.items():
            if not table in self._dbtables:
                self._create_table(table, content)
            if _compare_l1(content, self._table_columns(table)) and ecrase:
                self._delete_table(table)
                self._create_table(table, content)


class LicapyApiDB(object):

    __slots__ = ['dbmanager']

    def __init__(self, dbmanager=None):
        self.dbmanager = dbmanager

    def insert_object(self, object):
        pass

    def delete_object(self):
        pass

    def get_object_data(self, name):
        pass

    def setup_db_data(self, db):
        pass

def verify_database(dbname):
    return
