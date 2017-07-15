# Json test file
from greww.data.json.json_utils import create_json_file
from greww.data.basics import lsdir
print("kaka")
ftests = ['fist_test']


path="/home/ubuntu/greww/experience/op"

def fist_test():
    global path
    print('hello')
    create_json_file(directory=path, name="heyhey", kind=list)
    print('hello')
    assert "heyhey.json" in lsdir(path)

