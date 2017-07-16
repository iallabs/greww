from greww.settings import SETTINGS
from greww.data.basics import (lsdir,
                               stdir,
                               ckdir,
                               mkdir,
                               rmdir,
                               mkfile,
                               ckfile,
                               rmfile,
                               mkfile_with_content,
                               file_lenght,
                               file_size,
                               add_line_to_file,
                               add_lines_to_file,
                               del_lines_from_file,
                               replace_lines_in_file,
                               file_content)

pytests = ['test_dir_basics',
           'test_file_basics',
           'test_lines_operations']

ctests = []

_settings = SETTINGS("basics_tests", "ALL")

path = _settings["WORKING_DIRECTORY"]

test_dir = "greww_test_dir"

test_file= "loul"

ext="txt"

f = test_file + "." + ext

def test_dir_basics():
    stdir(path)
    mkdir(test_dir)
    assert test_dir in lsdir(path)
    assert ckdir(test_dir)
    rmdir(test_dir)
    assert not ckdir(test_dir)

def test_file_basics():
    stdir(path)
    mkfile(path, test_file, ext=ext)
    assert ckfile(path, f)
    rmfile(path, f)
    assert not ckfile(path, f)
    mkfile_with_content(directory=path, name=test_file, ext=ext, content=["test", "Greww", "greww"])
    assert ckfile(path, f)
    c = file_content(directory=path, name=f, expand=False).split("\n")
    assert "test" in c and "Greww" in c and "greww" in c
    assert not "Test" in c
    rmfile(path, f)


def test_lines_operations():
    pass


test_file_basics()
