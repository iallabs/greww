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
           'test_file_basics']

ctests = []

_settings = SETTINGS("basics_tests", "ALL")

path = _settings["WORKING_DIRECTORY"]

test_dir = "greww_test_dir"

test_file= "loul"

ext="txt"

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
    assert ckfile(path, test_file.join("." + ext))

test_dir_basics()
