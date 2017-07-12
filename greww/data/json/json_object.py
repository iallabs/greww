import json


def jsonize_kwargs(*args, **kwargs):
    A = list(args)
    keys = list(kwargs.keys())

    data = {
        "args" : A,
    }
    for k in keys:
        data[k] == kwargs[k]
    return data

def update_json_object(*args, obj=None, **kwargs):
    if _obj is None:
        raise #TODO
    obj = _obj
    if args:
        obj['args'] += list(args)
    if kwargs:
        for k in list(kwargs.keys()):
            obj[k] = kwargs[k]
    return obj
