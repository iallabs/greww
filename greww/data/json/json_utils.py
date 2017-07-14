import json
from greww.data.basics import (mkfile_with_content,
                               stdir)

import greww.data

def _ignore_c_settings():
    greww.data.C = False

def _make_c_settings():
    greww.data.C = True

def c_settings():
    return greww.data.C

#:TODO Rofl

#TODO: import settings

C_LIKE_SO = "greww/greww/cgreww/cjson.so"

DDEFAULT = ""

def create_json_file(directory=DDEFAULT, name=None, kind=None):
    ct = '[]' if kind == list else "{}"
    _mkfile_with_content(directory=directory,
                         name=name,
                         ext='json',
                         content=ct)

#Append for json list
def append_json_object(directory=DDEFAULT, name=None, json=None):
    if directory is none or name is None:
        return
        #TODO: Exception
    _stdir(directory)
    try:
        with open(name) as f:
            data = json.load(f)
            data.append(json)
        with open(name, 'w') as f:
            json.dump(data)

    except:
        raise Exception()
        #TODO: expetion

#Upload for json dict
def upload_json_object(directory=DDEFAULT, name=None, json=None):
    if directory is none or name is None:
        return
        #TODO: Exception
    _stdir(directory)
    try:
        with open(name) as f:
            data = json.load(f)
            data.upload(json)
        with open(name, 'w') as f:
            json.dump(data)

    except:
        raise Exception()
        #TODO: expetion

#XXX: this function actually works like all json files are list of json objects
def count_json_objects(directory=DDEFAULT, name=None):
    if directory is none or name is None:
        return
        #TODO: Exception
    _stdir(directory)
    try:
        with open(name) as f:
            data = json.load(f)
            return len(data)
    except:
        raise Exception()
        #TODO: expetion

#XXX: this function actually works like all json files are list of json objects
def del_json_object(directory=DDEFAULT, name=None, **kwargs):
    if directory is none or name is None:
        return
        #TODO: Exception
    if not kwargs:
        return
        #
    _stdir(directory)
    try:
        with open(name) as f:
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
    _rmfile(name)
    create_json_file(directory=directory,
                     name=name,
                     kind=list)
    try:
        with open(name, 'w') as f:
            json.dump(res, f)
    except:
        #TODO:
        return

def pythonize_json_file(directory=DDEFAULT, name=None):
    if directory is none or name is None:
        return
        #TODO: Exception
    try:
        with open(name) as f:
            data = json.load(f)
            return data
    except:
        #TODO:
        return
