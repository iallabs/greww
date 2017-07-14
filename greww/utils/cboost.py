import ctypes
from .exceptions import CppModuleImport, CppFunctionImport

Types= {'int' : ctypes.c_int,
         'char' : ctypes.c_char,
         'string' : ctypes.c_char_p}


# C++

import greww.utils as Q

t = Q.a


def call_cpp_function(func, path=None, out_put=None, in_put=None, op=None):
    if path is None:
        pass
    try:
        module = ctypes.CDLL(path)
    except:
        raise CppModuleImport(path)
    try:
        function = getattr(module, func)
    except:
        raise CppFunctionImport(module, func)

    if in_put:
        function.argstypes = [Types[i] if type(i) == str else i for i in in_put]
    if out_put:
        if type(out_put) == str:
            function.restype = Types[in_put]


    return function


#TODO: CPP Object
def call_cpp_object(obj, path=None):
    pass


# call_cpp_function(ked, path="/Users/ial/greww/greww/settings.so", out_put=ctypes.c_char_p)
"""
settings = ctypes.CDLL("/Users/ial/greww/greww/settings.so")
a=settings.ked
a.restype=ctypes.c_char_p
a.argstypes=[ctype.c_int]
print(a)

print(a())
"""
