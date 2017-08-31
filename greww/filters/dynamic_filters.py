def func_for_iter(filt):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            if hasattr(res, '__iter__'):
                return [filt(e) for e in res]
            return res
        return wrap_args
    return wrap_func


def filter_iter(res, _filter):
    return [_filter(e) for e in res]
