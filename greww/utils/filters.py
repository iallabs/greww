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

