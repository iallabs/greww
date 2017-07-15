import ctypes
import os
print(os.listdir())
module = ctypes.CDLL('/home/ubuntu/greww/greww/cgreww/export.so')
a=module.PyWrapper


a.argstypes=[ctypes.c_char_p]

a.restype=ctypes.c_char_p

print(a)

t=a("Export")

print(t)
