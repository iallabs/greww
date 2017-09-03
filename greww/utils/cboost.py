import ctypes
from .exceptions import CppModuleImport, CppFunctionImport


Types= {'int' : ctypes.c_int,
        'char' : ctypes.c_char,
        'string' : ctypes.c_char_p,
    	'stringlist' : ctypes.POINTER(ctypes.c_char_p),
	    'intlist' : ctypes.POINTER(ctypes.c_int)}


# C++


def call_cpp_function(func, path=None, out_put=None, in_put=None, args=None, kwargs=None):
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
