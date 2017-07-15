from greww.settings import SETTINGS
from greww.data.basics import (lsdir,
                               stdir,
                               chdir,
                               mkdir,
                               rmdir,
                               chkfile,
                               mkfile,
                               mkfile_with_content,
                               file_lenght,
                               file_size,
                               add_line_to_file,
                               add_lines_to_file,
                               del_lines_from_file,
                               replace_lines_in_file,
                               file_content)

ftests = ['test_basics']

DEFAULT="/home/ubuntu"

def test_basics():
    global DEFAULT
    print("directory ", basics.lsdir(DEFAULT))
    assert "greww" in basics.lsdir(DEFAULT)
