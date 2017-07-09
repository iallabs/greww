import ctypes


def call_cpp_function():
    pass

def make_cpp_function():
    pass



settings = ctypes.CDLL("/Users/ial/greww/greww/settings.so")
a=settings.ked
a.restype=ctypes.c_char_p
print(a)

print(a())
