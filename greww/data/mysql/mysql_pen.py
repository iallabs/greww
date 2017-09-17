from .mysql_utils import MysqlApiFunctions as MAF
from greww.utils.decorators import ClassDecorator #, ArgsBooster

_databases = ""

@ClassDecorator(decorator=staticmethod)
class MysqlPen(object):
    """
    This pen have a big d, can write everywhere.
    Errors raises if mysql raises one
    """
    __slots__ = [method for method in MAF.keys()]
    def __new__(cls):
        obj = object.__new__(cls)
        for method, func in MAF.items():
            setattr(obj,
                    method,
                    func)
        return obj

#@ClassDecorator(decorator=ArgsBooster(0, *_databases))
class AssertedMysqlPen(MysqlPen):
    """
    This pen have a short d, can't write anywhere
    Errors raises if he breaks it authorisations
    """
    __slots__ = ["_authorisation"] + [method for method in MAF.keys()]
    def __new__(cls, db):
        obj = object.__new__(cls)
        for method, func in MAF.items():
            setattr(obj,
                    method,
                    func)
