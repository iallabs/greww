#
import time
from lwa.databases.dbmanager import DBManager
from lwa.utils.decorators import _validpd
from lwa.utils.functions import _compare_l1
from lwa.databases.dataunit import DataUnit


class DBuilder(DBManager):
    # Licapy DataBase manager
    def __init__(self, cnxargs=(), db=LICAPY_DATABASES, show=True):
        DBManager.__init__(self, connection=None, connection_args=cnxargs)
        if self.state == 2:
            raise _NotAuthorisedOperation('DBuilder should connect to mysql')
        self.db = db
        if self._verify_db():
            if show: print('Licapy databases are all created in mysql!')
            for d in self.db:
                if self._verify_db_hierarchy(d):
                    if show: print('Database (', d, ') tables are set correctly')
                else:
                    if show: print('Database (', d, ') doesnt follow it protocol')

        else:
            if show: print('Not all Licapy databases are in mysql use ._build_db')
            if show: print('Processing co-builder')
            self._build_db()
            self._build_all_architecture()

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
        try:
            self.use_database(db)
        except:
            self.create_database(db)
            self.use_database(db)
        for table, content in architecture.items():
            if table in self._dbtables:
                if ecrase:
                    self._delete_table(table)
                    self._create_table(table=table, columns=content)
                continue
            self._create_table(table=table, columns=content)
        print('created db architecture for ', db)

    def _build_all_architecture(self):
        for _ in self.db:
            if _:
                self._build_db_architecture(_, ecrase=False)

    @property
    @_validpd
    def destroy_all(self):
        for _ in self.db:
            self.delete_database(_)

    @property
    def rebuild_database(self):
        self.destroy_all
        self._build_db()
        self._build_all_architecture()

#####################################

class LicapyDBManager(DBuilder):
    pass

def _fast_connect():
    return DBuilder(cnxargs=('localhost', 'root', 'uehMLMRw', ''), show=False)


def _register_request(date=time.ctime(), user='unknown', command=None):
    with _fast_connect() as lm:
        du = DataUnit(data=date, user=user, command=command, db='LicapyDB', table='RHistory')
        lm._add_value(DataUnit)

def _register_asroot(func):
    def pack_args(*args, **kwargs):
        _register_request(user='root', command=_quantify_commands(func=func, **kwargs))
        return func(*args, **kwargs)
    return pack_args

def _register(func, user=None):
    if user==None:
        return
    def pack_args(*args, **kwargs):
        _register_request(user=user, command=_quantify_commands(func=func, **kwargs))
        return func(*args, **kwargs)
    return pack_args

def _cache_order():
    with _fast_connect() as lm:
        du = DataUnit()
        pass

def _quantify_commands(**kwargs):
    return sum([str(i) + ':' + str(k) for k, i in kwargs.items()])
