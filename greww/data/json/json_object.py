from greww.data.basics import (mkfile_with_content,
			       stdir)
from greww.settings import SETTINGS
from greww.utils.cgreww import Greww
import json

_settings = SETTINGS(__name__, "ALL")

cgreww_settings = _settings("EVIRENEMENT")

DEFAULT_PATH = _settings["WORKING_DIRECTORY"]



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


def get_json_object(file=None, byid=None, **kwarg):
    pass
