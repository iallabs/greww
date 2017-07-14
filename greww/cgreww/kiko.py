import ctypes

module = ctypes.CDLL("export.so")

a=module.wrap_function

print(a)
