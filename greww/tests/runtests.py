import unittest
from greww.utils.runtime import timeit

all_modules = ['greww.data.tests.json_tests',
               'greww.data.tests.basics_tests']


def run_with_report(fn, utest=False):
    @timeit
    def tst(fn):
        if utest:
            func = unittest.FunctionTestCase(fn)
            func()
        else:
            fn()
    return tst(fn)

@timeit
def run_functions(*args):
    print('TEST START')
    for fnc in args:
        print('runing ...', fnc.__name__)
        run_with_report(fnc)
    print('TOTAL')

def run_pytests_modules(test_modules):
    for t in test_modules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['pytests'])
            suitefn = getattr(mod, 'pytests')
            functions = [getattr(mod, i) for i in suitefn]
            print(functions)
            run_functions(*functions)
        except:
            # else, just load all the test cases from the module.
            print('t - ', t)
            print('exception')

        #unittest.TextTestRunner().run(suite)
    print('end test')

def run_all_modules():
    run_pytests_modules(all_modules)

"""
#@rtdecorator
def run_functionszz(*funcs):
    f = list(funcs)
    for i in f:
        i()
    print('end')
"""

def run_all_tests():
    run_pytests_modules(all_modules)
