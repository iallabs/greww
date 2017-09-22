import json
from greww.data.basics import (set_dir,
                               remove_file,
                               check_file)
from greww.utils.exceptions import (WTF,
                                    LockedOption,
                                    NotImplementedAlgo)
import skmvs as SK

def make_json(directory=None, name=None, kind=dict, from_data=None, pretty=True):
    """
    Create json file at directory initiated as List Json or Dict Json
    =================================================================
    """
    if kind:
        ct = '[]' if kind == list else "{}"
    if from_data:
        ct = from_data
    set_dir(directory)
    if not ('.json' in name):
        name = '{0}.json'.format(name)
    f = open(name, 'w')
    if pretty:
        json.dump(ct, f,
                  sort_keys = True,
                  indent = 4,
                  ensure_ascii = False)
    else:
        json.dump(ct, f)
    f.close()

def feed_json(directory=None, name=None, obj=None):
    """
    feed json file at directory with obj
    =================================================================
    """
    if name is None:
        raise ValueError("Name can't be None")
    set_dir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
        if isinstance(data, list):
            data.append(obj)
        elif isinstance(data, dict):
            data.update(obj)
        else:
            raise WTF(file, data, obj)
    with open(name, 'w') as f:
        json.dump(data, f)

def count_json(directory=None, name=None):
    if name is None:
        raise ValueError("Name can't be None")
    set_dir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
        return len(data)

def unfeed_json(directory, name, **kwargs):
    """
    Remove all json objects under a json file that satify kwargs
    logic
    ==============================================================
    """
    if not kwargs:
        raise LockedOption("Unauthorized Move")
    set_dir(directory)
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
        remove_file(directory, name)
        with open(name, 'w') as f:
            json.dump(res, f)

    elif isinstance(data, list):
        #TODO: add this part
        raise NotImplementedAlgo(name)

def read_json(directory=None, name=None):
    """
    Read a json file to return a Python object
    ==============================================================
    """
    if name is None:
        raise ValueError("Name can't be None")
    set_dir(directory)
    with open(name, 'r') as f:
        data = json.load(f)
        return data

def search_json(directory, name, **kwargs):
    """
    Try to find a list of objects that satisfy kwargs logic
    ==============================================================
    """
    if name is None:
        raise ValueError("Name can't be None")
    set_dir(directory)
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
    elif isinstance(data, dict):
        #TODO: add this part
        raise NotImplementedAlgo(name)

def _replace_json(d, f, nc):
    """
    Replace json file content with another
    ==============================================================
    """
    remove_file(d, f)
    make_json(d, f, from_data=nc, pretty=True)

def jsonize_kwargs(*args, **kwargs):
    """
	Return a Json object that contain all data stored at args and kwargs
    ===================================================================
	"""
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
