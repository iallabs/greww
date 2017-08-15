import unittest
import time

test_modules = ['greww.data.tests.json_tests',
                'greww.data.tests.basics_tests',
                'greww.data.tests.mysql_tests']

def _test_function(function):
    try:
        t1 = time.time()
        function()
        t2 = time.time()
        print("[ OK ] ... {0} succeeded with a total run time of : {1} ms".format(function.__name__,
                                                                       t2 - t1))
    except:
        t2 = time.time()
        print("[WARN] ... {0} failed after runing {1} ms")

def import_module_tests_functions(module):
    mod = __import__(module, globals(), locals(), [''])
    functions = getattr(mod, '__all__')         #XXX: Python need this usless arguments
    return functions                            # to import all objects in a module

def run_pytests_modules(*test_modules):
    t1 = time.time()
    for module in test_modules:
        print("[INFO] ... Importing {0} test functions".format(module))
        functions = import_module_tests_functions(module)
        print("[INFO] ... Runing {0} test functions".format(module))
        print("[INFO] ... Total number of functions : {0}".format(len(functions)))
        k1 = time.time()
        for func in functions:
            _test_function(func)
        k2 = time.time()
        print("[INFO] ... Module tests total run time : {0} ms".format(k2 - k2))
        print("[INFO] ... --- end module tests ---")

    print('[INFO] ... --- end test ---')
    t2 = time.time()
    print('[ OK ] ... Total runtime : {0} ms'.format(t2 - t1))

def run_all_tests():
    run_pytests_modules(*test_modules)
