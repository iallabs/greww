import unittest

all_modules = []

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

def run_modules(test_module):
    for t in test_module:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['functions'])
            suitefn = getattr(mod, 'functions')
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
    run_modules(all_modules)


#@rtdecorator
def run_functionszz(*funcs):
    f = list(funcs)
    for i in f:
        i()
    print('end')

def run_test(path, func, timeit=False):
    # path format : pfbiology.core.tests.file_test-func
    b = path.split('.')
    eval('import ' + path)
    eval(b[-1] + '.func()')
    print('test_successfull')


def run_all_tests():
    run_modules(all_modules)
