from .mysql_utils import MysqlApiFunctions as MAF
from greww.utils.decorators import ClassDecorator


@ClassDecorator(decorator=staticmethod)
class MysqlPen(object):

    __slots__ = [method for method in MAF.keys()]

    def __new__(cls):
        obj = object.__new__(cls)
        for method, func in MAF.items():
            setattr(obj,
                    method,
                    func)
        return obj
