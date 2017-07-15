# Json test file
from greww.data.json.json_utils import create_json_file
from greww.data.basics import lsdir
from greww.settings import (SETTINGS,
                            activate_cgreww,
                            deactivate_cgreww,
                            activate_pygreww,
                            deactivate_pygreww)

pytests = ['test_json_file_creation',
           'test_json_object_creation',
           'test_json_object_append']

ctests = []

_settings = SETTINGS("json_utils", "ALL")

path = _settings["WORKING_DIRECTORY"]

#TODO: noobs write tests files
#CTESTS using greww.settings methods

def test_json_file_creation():
    global path
    create_json_file(directory=path, name="test_json_list", kind=list)
    assert "test_json_list.json" in lsdir(path)
    create_json_file(directory=path, name="test_json_dict", kind=dict)
    assert "test_json_dict.json" in lsdir(path)

def test_json_object_creation():
    pass

def test_json_object_append():
    pass

def test_json_object_read():
    pass

