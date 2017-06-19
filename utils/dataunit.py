from lwa.utils.functions import _certify

_default_tree = ('name', 'pname', 'type', 'id')
_default_data = ('name', 'location', 'synonyms')
dataunit_classes = set()
_dataunit_classes = []


class DataUnit(object):
    # Data unit store a dict of fields and their contents
    # at _args
    is_DataUnit = True
    table_format = []
    _name = 'default'

    __slots__ = ['_args', '_db', '_table']

    def __init__(self, db=None, table=None, **kwargs):
        self._args = kwargs
        self._db = db
        self._table = table

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name + ':' + self.name

    @property
    def name(self):
        try:
            return self._args['name']
        except:
            return

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
    table_format = _default_tree
    _name = 'TaxonUnit'
    pass

def _duclass_generator(classname, _format=_default_data):
    class _XDataUnit(DataUnit):
        table_format = _format
        _name = classname
        pass

    dataunit_classes.add(_XDataUnit)
    _dataunit_classes.append(_XDataUnit)
    return _XDataUnit
