from .cboost import call_cpp_function
import greww.utils
from .exceptions import DecaprecatedFunction
from .exceptions import MissingSettings


def _use_cpp_equivalent(name=None, sopath=None, args=None, kwargs=None):
    func_wrapper = call_cpp_function("PyWrapper",
                                     path=sopath,
                                     intput=['string', 'string'],
                                     output='stringlist')
    op, ip= func_wrapper(name, 'out_put'), func_wrapper(name, 'in_put')
    func = call_cpp_function(name,
                             path=sopath,
                             out_put=op,
                             in_put=ip)
    if not op:
        func(*args, **kwargs)
    else:
        return func(*args, **kwargs)



#Greww Decorator for all functions
def Greww(CActive=False, PActive=False, Decaprecated=False, sopath=None):
    def use_c_like(func):
        def wrap_args(*args, **kwargs):
            if Decaprecated:
                raise DecaprecatedFunction(func)
            elif PActive:
                return func(*args, **kwargs)
            elif CActive:
                if sopath is None:
                    raise MissingSettings(func)
                return _use_cpp_equivalent(name=func.__name__, sopath=sopath, args=args, kwargs=kwargs)
        return wrap_args
    return use_c_like


def ForceCGreww(func):
    pass

def DenyCGreww(func):
    pass

def OpenCGreww(func, C=False, P=False):
    pass


def RunTimeCGrew(func):
    pass

def make():
    return greww.utils.a

def change(p):
    greww.utils.a = p
