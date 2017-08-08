from .mysql_utils import MysqlApiFunction as MAF
from greww.utils.decorators import ClassDecorator



@ClassDecorator(decorator=classmethod)
class MysqlPen(object):

    __slots__ = [method.__name__ for method in MAF]

    def __new__(cls):
        obj = object.__new__(cls)
        for method in MAF:
            setattr(obj, method.name, method)
        return obj
