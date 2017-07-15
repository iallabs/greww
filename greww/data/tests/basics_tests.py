from greww.settings import SETTINGS
from greww.data.basics import (lsdir,
                               stdir,
                               ckdir,
                               mkdir,
                               rmdir,
                               mkfile,
                               mkfile_with_content,
                               file_lenght,
                               file_size,
                               add_line_to_file,
                               add_lines_to_file,
                               del_lines_from_file,
                               replace_lines_in_file,
                               file_content)

pytests = ['test_basics']

ctests = []

DEFAULT="/home/ubuntu"

def test_basics():
    global DEFAULT
    print("directory ", lsdir(DEFAULT))
    assert "greww" in lsdir(DEFAULT)
