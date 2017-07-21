import time
import timeout_decorator


INTERN_FAIL = -2
RUNTIME_FAIL = -3


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


