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
_ADD_COLLUMN =
_ADD_VALUE

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
    def databases(self):
        if self.state == 2:
            raise _NotAuthorisedMethod('You are already connected to a database *p3')
        with self.connection.cursor() as cursor:
            sql = _SHOW_DATA_BASES
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

    def create_table(self, tablename, collumns):
        pass

    def delete_table(self, tablename):
        pass

    def add_collumns(self, tablename, collumn):
        pass

    def del_collumn(self, tablename, collumn):
        pass

    def change_collumn(self, tablesname, collumn , new_collumns):
        pass

def verify_database(dbname):
    return
