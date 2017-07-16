import json
from greww.data.basics import (mkfile_with_content,
                               stdir,
                               rmfile,
                               ckfile)
from greww.settings import SETTINGS
from greww.utils.cgreww import Greww

#:TODO Rofl

#TODO: import settings

_settings = SETTINGS("json_utils", "ALL")

cgreww_settings = _settings["ENVIRENEMENT"]

DEFAULT_PATH = _settings["WORKING_DIRECTORY"]

#@Greww(**cgreww_settings)
def create_json_file(directory=DEFAULT_PATH, name=None, kind=None):
    ct = '[]' if kind == list else "{}"
    mkfile_with_content(directory=directory,
                         name=name,
                         ext='json',
                         content=ct)

#Append for json list
def append_json_object(directory=DEFAULT_PATH, name=None, obj=None):
    if directory is None or name is None:
        return
        #TODO: Exception
    stdir(directory)
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            data.append(obj)
        with open(name, 'w') as f:
            json.dump(data, f)

    except:
        raise Exception()
        #TODO: expetion

#Upload for json dict
def upload_json_object(directory=DEFAULT_PATH, name=None, obj=None):
    if directory is None or name is None:
        return
        #TODO: Exception
    stdir(directory)
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            data.upload(obj)
        with open(name, 'w') as f:
            json.dump(data, f)

    except:
        raise Exception()
        #TODO: expetion

#XXX: this function actually works like all json files are list of json objects
def count_json_objects(directory=DEFAULT_PATH, name=None):
    if directory is None or name is None:
        return
        #TODO: Exception
    stdir(directory)
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            return len(data)
    except:
        raise Exception()
        #TODO: expetion

#XXX: this function actually works like all json files are list of json objects
def del_json_object(directory=DEFAULT_PATH, name=None, **kwargs):
    if directory is None or name is None:
        return
        #TODO: Exception
    if not kwargs:
        return
        #
    stdir(directory)
    try:
        with open(name, 'r') as f:
            data = json.load(f)
    except:
        #TODO:
        return
    i = 0
    res = []
    for obj in data:
        i += 1
        for k in list(kwargs.keys()):
            if not obj[k] == kwargs[k]:
                res.append(obj)
                continue
    rmfile(directory, name)
    with open(name, 'w') as f:
        json.dump(res, f)


def pythonize_json_file(directory=DEFAULT_PATH, name=None):
    if directory is None or name is None:
        return
        #TODO: Exception
    try:
        with open(name, 'r') as f:
            data = json.load(f)
            return data
    except:
        #TODO:
        return

def get_json_object_from_file(directory=DEFAULT_PATH, name=None, **kwargs):
    if directory is None or name is None:
        return -1
        #TODO: Exception
    stdir(directory)
    if not ckfile(directory, name):
        return -1
        #TODO: Exception
    with open(name, 'r') as f:
        data = json.load(f)
    import collections
    #FIXME: add possibility to get objects from one main json_object
    results = []
    w = True
    for i in data:
        for k in list(kwargs.keys()):
            if i[k] != kwargs[k]:
                w = False
                break
        if w:
             results += [i]
        w = True
    return results
