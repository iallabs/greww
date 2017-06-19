def _firstraws(func):
    def pick_args(*args, **kwargs):
        result = func(*args, **kwargs)
        if result:
            return [i[0] for i in result]
        return []
    return pick_args

def _validpd(func):
    def pick_args(*args, **kwargs):
        print('passord : NOPASSWORD')
        result = func(*args, **kwargs)
        return result
    return pick_args

def _forall(func):
    def pick_args(*args, **kwargs):
        if args:
            for i in args:
                if i:
                    print('pickled to function', i)
                    result = func(*i, **kwargs)
        return result
    return pick_args

def _cacheit(func):
    pass
