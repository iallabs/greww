import mysql.connector
from greww.vmfetcher import MachineIdentity as MID
from greww.utils.exceptions import (BadConnector,
                                    RejectedConnection)

MYSQL_LOGS = MID._load("mysql.logs")
MYSQL_CONFIG = MID._load("mysql.config")

class ConnectorsGenerator():

    __slots__ = ["connectors"]

    def __init__(self):
        self.connectors = set()

    @property
    def gen(self):
        return self.connectors.copy().pop()

    @property
    def is_empty(self):
        return len(self.connectors) == 0

    def _register(self, cntr):
        self.connectors.add(cntr)

    def _new(self):
        self.connectors.add(mysql_local_connector())

    def _reset(self):
        self.connectors.clear()
        self._new()

_connectors = ConnectorsGenerator()

def connector_register(func):
    global _connectors
    c = func()
    _connectors._register(c)
    return c

def with_connectors_register(func):
    def wrap_args(*args,**kwargs):
        global _connectors
        if _connectors.is_empty:
            _connectors._new()
        kwargs["connector"] = _connectors.gen
        res = func(*args, **kwargs)
        return res
    return wrap_args

def pure_connector_underfails(*exceptions):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except execptions:
                kwargs["connector"] = mysql_local_connector()
                return func(*args, **kwargs)
            return res
        return wrap_args
    return wrap_func

@connector_register
def mysql_local_connector():
    """
    Return "LOCAL" MySQLConnection Cursor object
    ======================================================
    """
    try:
        global MYSQL_LOGS, MYSQL_CONFIG
        use_pure = MYSQL_CONFIG['use_pure']
        raise_on_warnings = MYSQL_CONFIG['raise_on_warnings']
        host = MYSQL_LOGS['host']
        user = MYSQL_LOGS['user']
        password = MYSQL_LOGS['password']
        c = mysql.connector.connect(host=host,
                                    user=user,
                                    password=password,
                                    use_pure=use_pure,
                                    raise_on_warnings=raise_on_warnings)
        return c
    except:
        raise RejectedConnection(logs=MYSQL_LOGS, cnf=MYSQL_CONFIG)

@pure_connector_underfails(BadConnector)
@with_connectors_register
def execute_only(*args, commit=False, connector=None):
    """
    Execute a serie of queries to known cursor
    =====================================================
    >>> from zilean import execute_sql
    >>> from zilean import mysql_local_connection
    >>> crs = m()
    >>> execute_sql(query1, query2, cursor=crs).__call__()
    { "result" : '', "status" : -9999}
    =====================================================
    """
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    if commit:
        connector.commit()

@pure_connector_underfails(BadConnector)
@with_connectors_register
def execute_and_fetch(*args, commit=False, connector=None):
    """
    Execute a serie of queries to known cursor
    =====================================================
    >>> from zilean import execute_sql
    >>> from zilean import mysql_local_connection
    >>> crs = m()
    >>> execute_sql("SHOW DATABASE", cursor=crs)
    [('information_schema',), ('mysql',), ('performance_schema',), ('sys',), ('zileansystem',)]
    =====================================================
    """
    result = []
    try:
        cursor = connector.cursor()
    except:
        raise BadConnector(connector)
    for query in list(args):
        cursor.execute(query)
    for e in cursor:
        result.append(e)
    if commit:
        connector.commit()
    return result
