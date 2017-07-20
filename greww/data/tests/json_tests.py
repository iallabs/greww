# Json test file
from greww.data.json.json_utils import (create_json_file,
                                        append_json_object,
                                        count_json_objects,
                                        del_json_object,
                                        pythonize_json_file,
                                        get_json_object_from_file)

from greww.data.json.json_object import (jsonize_kwargs,
                                         update_json_object)
from greww.data.basics import (lsdir,
                               stdir,
                               ckfile,
                               file_content,
                               file_lenght,
                               rmfile)

from greww.settings import (SETTINGS,
                            activate_cgreww,
                            deactivate_cgreww,
                            activate_pygreww,
                            deactivate_pygreww)

pytests = ['test_json_file_creation',
           'test_json_object_creation',
           'test_json_object_append',
           'test_json_object_delete',
           'test_json_object_read']

ctests = []

_settings = SETTINGS("json_utils", "ALL")

path = _settings["WORKING_DIRECTORY"]

#TODO: noobs write tests files
#CTESTS using greww.settings methods
t1 = "td"
t2 = "tl"
t1x = "td.json"
t2x = "tl.json"


def test_json_file_creation():
    stdir(path)
    create_json_file(directory=path, name=t1, kind=list)
    create_json_file(directory=path, name=t2, kind=dict)
    assert ckfile(path, t1x)\
           and ckfile(path, t2x)
    c1 = file_lenght(directory=path, name=t1x)
    c2 = file_lenght(directory=path, name=t1x)
    assert c1 == 1\
           and c2 == 1
    rmfile(path, t1x)
    rmfile(path, t2x)

data = jsonize_kwargs("Net", "Kappa", name="newbie", age=5)

def test_json_object_creation():
    k = list(data.keys())
    assert "args" in k\
           and "name" in k\
           and "age" in k
    t = list(data.values())
    assert "newbie" in t\
           and 5 in t\
           and "Net" in data["args"]\
           and "Kappa" in data["args"]
    data2 = update_json_object("lol", obj=data, gender="troll")
    k = list(data.keys())
    assert "args" in k\
           and "name" in k\
           and "age" in k\
           and "gender" in k
    t = list(data.values())
    assert "newbie" in t\
           and "troll" in t\
           and 5 in t\
           and "Net" in data["args"]\
           and "Kappa" in data["args"]\
           and "lol" in data["args"]

def test_json_object_append():
    create_json_file(directory=path, name="jlist", kind=list)
    append_json_object(directory=path, name="jlist.json", obj=data)
    assert count_json_objects(path, "jlist.json") == 1
    append_json_object(directory=path, name="jlist.json", obj=data)
    assert count_json_objects(path, "jlist.json") == 2
    rmfile(path, "jlist.json")

def test_json_object_delete():
    create_json_file(directory=path, name="jlist", kind=list)
    append_json_object(directory=path, name="jlist.json", obj=data)
    del_json_object(directory=path, name="jlist.json", gender="male", age=5)
    assert count_json_objects(path, "jlist.json") == 1
    del_json_object(directory=path, name="jlist.json", age=5)
    assert count_json_objects(path, "jlist.json") == 0
    rmfile(path, "jlist.json")

def test_json_object_read():
    create_json_file(directory=path, name="jlist", kind=list)
    append_json_object(directory=path, name="jlist.json", obj=data)
    data2 = get_json_object_from_file(directory=path, name="jlist.json", age=6)
    assert not data2
    data2 = get_json_object_from_file(directory=path, name="jlist.json", age=5, gender="kikou")
    assert not data2
    data2 = get_json_object_from_file(directory=path, name="jlist.json", age=5, gender="troll")
    assert len(data2) > 0
    rmfile(path, "jlist.json")

test_json_file_creation()
test_json_object_creation()
test_json_object_append()
test_json_object_delete()
test_json_object_read()
