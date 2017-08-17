import json
from greww.data.basics import (mkfile_with_content,
                               stdir,
                               rmfile,
                               ckfile)
from greww.utils.exceptions import (WTF,
                                    LockedOption,
                                    NotImplementedAlgo)
from greww.shellenv import import_varenv


GWP = import_varenv("GREWW_WORKING_PATH")

def make_json(directory=GWP, name=None, kind=None, from_data=None):
    """
    Create json file at directory initiated as List Json or Dict Json
    =================================================================
    """
    if kind:
        ct = '[]' if kind == list else "{}"
    if from_data:
        ct = from_data
    mkfile_with_content(directory=directory,
                        name=name,
                        ext='json',
                        content=ct)


def feed_json(directory=GWP, name=None, obj=None):
    if name is None:
        raise ValueError("Name can't be None")
    stdir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
        if isinstance(data, list):
            data.append(obj)
        elif isinstance(data, dict):
            data.upload(obj)
        else:
            raise WTF(file, data, obj)
    with open(name, 'w') as f:
        json.dump(data, f)

def count_json(directory=GWP, name=None):
    if name is None:
        raise ValueError("Name can't be None")
    stdir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
        return len(data)

def unfeed_json(directory=GWP, name=None, **kwargs):
    """
    Remove all json objects under a json file that satify kwargs
    logic
    ==============================================================
    """
    if directory is None or name is None:
        raise ValueError("Name can't be None")
    if not kwargs:
        raise LockedOption("Unauthorized Move")
    stdir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
    if isinstance(data, list):
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

    elif isinstance(data, list):
        #TODO: add this part
        raise NotImplementedAlgo(name)

def read_json(directory=GWP, name=None):
    """
    Read a json file to return a Python object
    ==============================================================
    """
    if name is None:
        raise ValueError("Name can't be None")
    with open(name, 'r') as f:
        data = json.load(f)
        return data

def search_json(directory=GWP, name=None, **kwargs):
    """
    Try to find a list of objects that satisfy kwargs logic
    ==============================================================
    """
    if name is None:
        raise ValueError("Name can't be None")
    stdir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
    results = []
    w = True
    if isinstance(data, list):
        for i in data:
            for k in list(kwargs.keys()):
                if i[k] != kwargs[k]:
                    w = False
                    break
            if w:
                 results += [i]
            w = True
        return results

    elif isinstance(data, list):
        #TODO: add this part
        raise NotImplementedAlgo(name)
