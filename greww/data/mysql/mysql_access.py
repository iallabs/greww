import mysql.connector
from greww._machine_config import MachineIdentity as MID
from greww.utils.exceptions import (BadConnector,
                                    RejectedConnection)


def mysql_local_connector():
    """
    Return "LOCAL" MySQLConnection Cursor object
    ======================================================
    """
    try:
        MYSQL_LOGS = MID._load("mysql.logs")
        MYSQL_CONFIG = MID._load("mysql.config")
        #XXX: The reason behind creting each parameter in
        # Variables is because Python doesnt support 2 concated
        # Dictionaries untill version >=3.x
        # example :
        # c = mysql.connector.connect(host)
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

class ConnectorsGenerator(object):

    __slots__ = ["connectors"]

    def __init__(self):
        self.connectors = set()
        self._new()

    @property
    def gen(self):
        return self.connectors.copy().pop()

    @property
    def is_empty(self):
        return len(self.connectors) == 0

    def _register(self, cntr):
        self.connectors.add(cntr)

    def _new(self):
        c = mysql_local_connector()
        self.connectors.add(c)

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
            except exceptions:
                kwargs["connector"] = mysql_local_connector()
                return func(*args, **kwargs)
            return res
        return wrap_args
    return wrap_func


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
