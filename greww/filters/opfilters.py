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
