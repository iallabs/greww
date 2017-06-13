from lwa.databases.dbmanager import DBManager
from lwa.utils.decorators import _validpd
from lwa.utils.functions import _compare_l1

LICAPY_DATABASES = ['Plantae',
                    'Animalia',
                    'Fungi',
                    'Chromista',
                    'Virus',
                    'Bacteria',
                    'EssentialOils',
                    'VegatalOils',
                    'LicapyDB']


PLANTAE_DB = {'PlantTree' : ('name', 'pname', 'type', 'id'),
              'PlantData' : ('name', 'location', 'morphology', 'synonyms')}

ANIMALIA_DB = {'AnimalTree' : ('name', 'pname', 'type', 'id'),
               'AnimalData' : ('name', 'location', 'morphology', 'synonyms')}

FUNGI_DB = {'FungiTree' : ('name', 'pname', 'type', 'id'),
            'FungiData' : ('name', 'location', 'morphology', 'synonyms')}

CHROMISTA_DB = {'ChromistaTree' : ('name', 'pname', 'type', 'id'),
                'ChromistaData' : ('name', 'location', 'morphology', 'synonyms')}

VIRUS_DB = {'VirusTree' : ('name', 'pname', 'type', 'id'),
            'VirusData' : ('name', 'pathology', 'origine', 'morphology', 'synonyms')}

BACTERIA_DB = {'BacteriaTree' : ('name', 'pname', 'type', 'id'),
               'BacteriaData' : ('name', 'pathology', 'origine', 'morphology', 'synonyms')}

ESSENTIAL_OILS_DB = {'EssoilTree' : ('name', 'pname', 'type', 'id'),
                     'EssoilData' : ('name', 'pathology', 'origine','morphology', 'synonyms')}

VEGETAL_OILS_DB = {'VegoilTree' : ('name', 'pname', 'type', 'id'),
                   'VegoilData' : ('name', 'pathology', 'origine', 'morphology', 'synonyms')}

LICAPY_DB = {'LicapyAdmins' : ('user', 'password', 'name', 'email')}

LICAPY_DATABASES_EXPANDS = [PLANTAE_DB,
                            ANIMALIA_DB,
                            FUNGI_DB,
                            CHROMISTA_DB,
                            VIRUS_DB,
                            BACTERIA_DB,
                            ESSENTIAL_OILS_DB,
                            VEGETAL_OILS_DB,
                            LICAPY_DB]

class LicapyDBManager(DBManager):
    # Licapy DataBase manager
    def __init__(self, cnxargs=(), db=LICAPY_DATABASES, show=True):
        DBManager.__init__(self, connection=None, connection_args=cnxargs)
        if self.state == 2:
            raise _NotAuthorisedOperation('LicapyDBManager should connect to mysql')
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
                    self._create_table(table, content)
                continue
            self._create_table(table, content)
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

Authorised_users = []

requests = {'connect' : None,
            'exit' : None,
            'adata' : None,
            'gdata' : None,
            'gbuild' : None,
            'scan' : None,
            'stats' : None}

class LicapyApi(object):

    __slots__ = []

    def __init__(self, cnxargs=()):
        if not cnxargs:
            self._show_authorised_users()
            self._exit()
        self.dbmanager = dbmanager

    @property
    def _connect(self):
        pass

    @property
    def _exit(self):
        pass

    def _request(self, request=None):
        pass
