import json
import os

def set_direction(direction):
    os.chdir(direction)

#:TODO Rofl

def add_element_to_json_list(element, _file , direction=default):
    set_direction(direction)
    try:
        with open(_file) as f:
            data = json.load(f)
            data.append(element)
        with open(_file, 'w') as f:
            json.dump(data, f)
    except:
        err = 'file dosent exist'
        raise Exception(err)

def add_element_to_json_dict(element, _file , direction=default, _type=None):
    if _type is None:
        return
    set_direction(direction)
    try:
        with open(_file) as f:
            data = json.load(f)
            if _type == list:
                data.append(element)
            elif _type == dict:
                data.upload(element)
            else:
                err = 'NotImplemented'
                raise Exception(err)
        with open(_file, 'w') as f:
            json.dump(data, f)
    except:
        err = 'file dosent exist'
        raise Exception(err)

def count_json_objects(fl, direction=default, rlo=False):
    set_direction(direction)
    if not fl:
        err = ("file is None")
        raise Exception(err)
    with open(fl) as f:
        gen = json.loads(f.read())
    res = []
    count = 0
    bjj = None
    for obj in gen:
        if obj["instance"]:
            count += 1
            bjj = obj["instance"]
    if rlo:
        return count, bjj
    return count
