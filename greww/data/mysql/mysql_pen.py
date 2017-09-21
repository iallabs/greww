from .mysql_utils import MysqlApiFunctions as MAF
from greww.utils.decorators import ClassDecorator #, ArgsBooster

_databases = ""

@ClassDecorator(decorator=staticmethod)
class _MysqlPen(object):
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

MysqlPen = _MysqlPen()

#@ClassDecorator(decorator=ArgsBooster(0, *_databases))
class _AssertedMysqlPen(_MysqlPen):
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

AssertedMysqlPen = _AssertedMysqlPen("kaka")
