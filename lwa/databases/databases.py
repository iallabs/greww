# this is databases connector to python

import pymysql.cursors

databases = ['testdb']

class _ConnectionFailled(Exception):
    pass

class _NotAuthorisedMethod(Exception):
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
_DELETE_DATA_BASE = "DROP DATABASE {0}"
_USE_DATA_BASE = "USE {0}"
_SHOW_TABLE = "DESC {0}"
_SHOW_ALL_TABLES = "show tables;"
_CREATE_TABLE = "CREATE TABLE {0} ({1});"
_ADD_COLLUMN = ""
_DELETE_TABLE = ""
_ADD_VALUE = ""
_INSERT_VALUE = ""

_protocol_noprotocol = ' VARCHAR(10) NOT NULL,'
_protocol_taxon = {'s' : ' VARCHAR(10) NOT NULL,',
                   'i' : ' INT NOT NULL,',
                   'p' : ' PRIMARY KEY {0}'}

def _query_create_table(name, fields):
    _funquery = ''
    for field in fields:
        if ':' in field:
            field, code = field.split(':'))
            _funquery += ' ' + field
            for c in code:
                _funquery += _protocol_taxon[c]
                if field != fields[-1]:
                    _funquery += ','
            continue
        _funquery += ' ' + field + _protocol_noprotocol
        if field != fields[-1]:
            _funquery += ','
    _query = _CREATE_TABLE.format(name, _funquery)

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
        with self.connection.cursor() as cursor:
            sql = _DELETE_DATA_BASE.format(dbname)
            cursor.execute(sql)
            print('Deleted database : ', dbname)

    def use_database(self, name):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *m6')
        with self.connection.cursor() as cursor:
            sql = _DELETE_DATA_BASE.format(dbname)
            cursor.execute(sql)
            print('Deleted database : ', dbname)

    def _table_columns(self, table):
        pass

    def _create_table(self, tablename, collumns):
        pass

    def _delete_table(self, tablename):
        pass

    def _add_columns(self, tablename, collumn):
        pass

    def _del_column(self, tablename, collumn):
        pass

    def _change_column(self, tablesname, collumn , new_collumns):
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

PLANTAE_DB = {'TreeData' : ('id', 'name', 'pname', 'level'),
              'PlantsData' : ('id', 'name', 'pname', 'locations', 'caracteristiques')}

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
