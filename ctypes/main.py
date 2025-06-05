import ctypes

#load the compiled C library
lib = ctypes.CDLL('./math_ops.co')

# specify arguments/return types
lib.factorial.argtypes = [ctypes.c_int]
lib.factorial.restypes = ctypes.c_longlong

# call like a python function
print(lin.factorial(10)) # output: 3628800
