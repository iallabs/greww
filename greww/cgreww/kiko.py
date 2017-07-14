import ctypes

module = ctypes.CDLL("export.so")
a=module.PyWrapper


a.argstypes=[ctypes.c_char_p]
a.restype=ctypes.c_char_p


t=a("Export")

print(t)
