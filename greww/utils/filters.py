# greww filters

#> decorate function with 2 dimentional return value
#> indexes is a list if integers

def tuplik(e, indexes):
    if len(e) == 1:
        return e[0]
    else:
        R = [e[i] for i in indexes]
        if len(R) == 1:
            return R[0]
        return R

def filter_app(filt=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            _res = []
            for i in res:
                _res += [filt(i)]
            return _res
        return wrap_args
    return wrap_func


def refetch_filter(indexes):
    """
    Decorator that treates 2D List and return only raws
    indexes
    ===================================================
    >>> f(2)
    [(0, 1, 2), (1, 2, 3)]
    >>> _refetch_filter([0, 2])f(2)
    [(0, 2), (1, 3)]
    ====================================================
    """
    def wrap_func(func):
        if not indexes:
            return func
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            ress = []
            for i in res:
                ress.append(tuplik(i, indexes))
            return ress
        return wrap_args
    return wrap_func


def rezip_filter(res_type=list, split_opt="=", applied_func=None):
    """
    """
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            dicta = {}
            if not isinstance(res, res_type):
                return res
            for i in res:
                val = applied_func(i)
                if not ('=' in val) or val.count('=') > 1:
                    continue
                _d, _v = val.split(split_opt)
                dicta.update({_d: _v})
            return dicta
        return wrap_args
    return wrap_func


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
