import unittest
import time

"""
         69696969                         69696969
       6969    696969                   696969    6969
     969    69  6969696               6969  6969     696
    969        696969696             696969696969     696
   969        69696969696           6969696969696      696
   696      9696969696969           969696969696       969
    696     696969696969             969696969        969
     696     696  96969      _=_      9696969  69    696
       9696    969696      q(-_-)p      696969    6969
          96969696         '_) (_`         69696969
             96            /__/  \            69
             69          _(<_   / )_          96
            6969        (__\_\_|_/__)        9696
    =======================================================
"""


test_modules = ['greww.data.tests.tests_basics',
                'greww.data.tests.tests_json',
                'greww.data.tests.tests_mysql']

Succeeded_Test = "[ OK ] ... {0} succeeded ES:{1} with a total run time of : {2} ms"
Failed_Test = "[WARN] ... {0} failed after runing : {1} ms"

def _test_function(func):
    try:
        t1 = time.time()
        exit_status = func()
        t2 = time.time()
        print(Succeeded_Test.format(func.__name__, exit_status, t2 - t1))
    except:
        t2 = time.time()
        print(Failed_Test.format(func.__name__, t2 - t1))
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
        print("[INFO] ... Module tests total run time : {0} ms".format(k2 - k1))
        print("[INFO] ... --- end module tests ---")

    print('[INFO] ... --- end test ---')
    t2 = time.time()
    print('[ OK ] ... Total runtime : {0} ms'.format(t2 - t1))

def run_all_tests():
    run_pytests_modules(*test_modules)
