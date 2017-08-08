from greww.data.basics import (mkfile_with_content,
			       			   stdir,
                               file_content)
import json




def jsonize_kwargs(*args, **kwargs):
    #A = list(args)
    keys = list(kwargs.keys())
    if not args:
        data = kwargs
    else:
        data = {
             "args" : list(args),
        }
        for k in keys:
            data[k] = kwargs[k]
    return data

def update_json_object(*args, **kwargs):
    if kwargs["obj"] is None:
        raise Exception()#TODO
    obj=kwargs["obj"]
    if args:
        obj['args'] += list(args)
    if kwargs:
        for k in list(kwargs.keys()):
            if k == "obj":
                continue
            obj[k] = kwargs[k]
    return obj


def get_json_object(file=None, byid=None, **kwarg):
    pass
