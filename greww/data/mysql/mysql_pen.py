from .mysql_utils import MysqlApiFunction as MAF
from greww.utils.decorators import ClassDecorator


@ClassDecorator(decorator=staticmethod)
class MysqlPen(object):

    __slots__ = [method.__name__ for method in MAF]

    def __new__(cls):
        obj = object.__new__(cls)
        for method in MAF:
            setattr(obj,
                    method.__name__,
                    method)
        return obj
