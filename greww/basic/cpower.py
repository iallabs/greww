import ctypes
settings = ctypes.CDLL("/Users/ial/greww/greww/settings.so")
a=settings.vrcaller
a.argtypes = [ctypes.c_char_p]
a.restype = ctypes.c_char_p

print(a('amine'))
