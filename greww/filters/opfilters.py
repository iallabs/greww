# greww filters


#> decorate function with 2 dimentional return value
#> indexes is a list if integers

def refetch_filter(indexes):
    """
    Decorator that treates 2D List and return only raws
    indexes
    ===================================================
    >>> f = lambda n: [(x, x+1, x+2), -9999)\
                       for x in range(n)]
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
                ress += tuplik(*[i[j] for j in indexes])
            return ress
        return wrap_args
    return wrap_func
