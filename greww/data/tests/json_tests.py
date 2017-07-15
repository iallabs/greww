# Json test file
from greww.data.json.json_utils import SETTINGS, create_json_file
from greww.data.basics import lsdir
ftests = ['fist_test']


path="/home/ubuntu/greww/experience/op"

def fist_test():
    create_json_file(directory=path, name=heyhey, kind=list)
    assert "heyhey.json" in lsdir(path)

