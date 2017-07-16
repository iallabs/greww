from greww.data.basics import (mkfile_with_content,
			       stdir,
                               file_content)
from greww.settings import SETTINGS
from greww.utils.cgreww import Greww
import json

f = __file__.split("/")[-1]
f = f.split(".")[1]

_settings = SETTINGS("json_object", "ALL")

cgreww_settings = _settings["ENVIRENEMENT"]

DEFAULT_PATH = _settings["WORKING_DIRECTORY"]


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

def update_json_object(*args, obj=None, **kwargs):
    if obj is None:
        raise #TODO
    if args:
        obj['args'] += list(args)
    if kwargs:
        for k in list(kwargs.keys()):
            obj[k] = kwargs[k]
    return obj


def get_json_object(file=None, byid=None, **kwarg):
    pass

