# greww filters


#> decorate function with 2 dimentional return value
#> indexes is a list if integers
def _filter_raws(indexes=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            if not indexes:
                return res
            ret = []
            if len(indexes) == 1:
                ret = [i[0] for i in res]
            else:
                for i in res:
                    line = [i[k] for k in indexes]
                    ret += line
            return ret
        return wrap_args
    return wrap_func


def _refetch_filter(indexes):
    """
    Decorator to functions that out put a ZileanOP to
    reselect mostly mysql tuple out_puts in result list
    ===================================================
    >>> f = lambda n: [ZileanOP((x, x+1, x+2), -9999)\
                       for x in range(n)]
    >>> f(2).
    [(0, 1, 2), (1, 2, 3)]
    >>> nf = _refetch_filter([0, 2])f(2)
    [(0, 2), (1, 3)]
    ====================================================
    """
    def wrap_func(func):
        if not indexes:
            return func
        def wrap_args(*args, **kwargs):
            res = func(*args, **kwargs)
            ress = []
            try:
                for i in res.result:
                    ress += tuplik(*[i[j] for j in indexes])
                    res.result, res.status = ress, -9998
                return res
            except:
                res.status = -8
                return res
        return wrap_args
    return wrap_func
