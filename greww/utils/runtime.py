import time
import errno
import signal
import timeout_decorator
from functools import wraps
from .decorators import ClassDecorator


def calculate_run_time(func, loop=1):
    t1 = time.time()
    eval(func.__name__ + '()')
    t2 = time.time()
    return 'run in :'+ str(t2 - t1) + ' ms'


def timeit(func, active=True):
    def timed(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        if active:
            print('run time method* : ' + str(t2 - t1) + ' ms')
        return result
    return timed

# timedN
# run func with it args N time in order to detect unsual
# runtime differences
def timeitN(func, loop=1, report=True, active=True):
    def analyse(ln):
        an = []
        dn = []
        for i in range(0, len(ln) - 1):
            an += [ln[i + 1] - ln[i]]
        moy = sum(an) / len(an)
        for i in an:
            dn += [moy - i]
        return an, dn, moy

    def timedN(*args, **kwargs):
        t_records = [time.time()]
        for i in range(loop):
            result = func(*args, **kwargs)
            t_records += [time.time()]
        an, dn, moy = analyse(t_records)
        if active:
            print('run times for ' + str(loop) + ' times :', an)
            print('average run time ' + str(moy))
            print('diff run time from avg', an)
            print('total run time :' + sum(an))
        else:
            print('total run time :' + sum(an))
            print('avg ' + moy)

def timeout(seconds=10, error_message="lol"):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wraps(func)(wrapper)
    return decorator


def ctrl_runtime(limit=None, case_pass=None, case_timeout=-3, case_fail=-1, on_sub_process=False):
    def wrap_function(func):
        def wrap_param(*args, **kwargs):
            result = None
            if on_sub_process:
                timed_fund = timeout_decorator.timeout(limit, use_signals=False)(func)
            else:
                timed_func = timeout_decorator.timeout(limit)(func)
            try:
                result = time_func(*args, **kwargs)
                if case_pass:
                    return case_pass
                return result
            except TimeoutError:
                return case_timeout
            except:
                return case_fail
        return wrap_param
    return wrap_function

_dec = [timeout,
        timeit,
        timeitN]

@ClassDecorator(classmethod)
class GrewwTimers(object):
    pass
