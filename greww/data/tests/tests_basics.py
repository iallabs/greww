from greww.data.basics import (list_dir,
                               set_dir,
                               check_dir,
                               make_dir,
                               remove_dir,
                               find_dir,
                               check_file,
                               find_file,
                               make_file,
                               check_file,
                               remove_file,
                               mkfile_with_content,
                               file_content,
                               file_lenght,
                               add_line,
                               add_lines,
                               del_lines,
                               replace_lines,
                               file_size)

#from greww._envs import GREWW_CACHE, GREWW_PATH
import os
GC = "/Users/ial-ah/GitHub/greww/cache"
GP = "/Users/ial-ah/GitHub/greww"

TDIR = "{0}/tests".format(GC)
TFILE = "test1"
TFILES = ["kikou",
          "kikoutee",
          "zaza"]
TDIRS = ["dtest",
         "flip",
         "flap"]

def test_dir_file_basics():
    # check cache dir
    assert check_dir(GC)
    make_dir(TDIR)
    # make test dir
    assert check_dir(TDIR)
    # list dir
    d = list_dir(GC)
    assert TDIR in d
    # set dir
    set_dir(GP)
    d = list_dir('cache')
    assert TDIR in d
    set_dir(TDIR)
    # make dirs
    make_dir('testdir8')
    make_dirs('testdir9')
    set_dir(GP)
    # find dir
    pd = find_dir('testdir8')
    assert pd == TDIR + 'testdir8'
    # remove dir
    remove_dir(TDIR + 'testdir8')
    # reove dir rec
    remove_dir(TDIR, rec=True)
    pd = find_dir('testdir8')
    assert not pd
    # reconstrcut
    make_dir(TDIR)
    set_dir(TDIR)
    make_dir('testdir8')
    make_dirs('testdir9')
    # make file
    make_file(TDIR + TFILE)
    # check file
    assert check_file(TDIR + TFILE)
    make_file(TDIR + 'testdir9' + TFILE)
    # find_file
    pf = find_file('TFILE')
    assert len(pf) == 2
    # remove file
    remove_file(TDIR + 'testdir9' + TFILE)
    pf = find_file('TFILE')
    assert len(pf) == 1
    # remove
    remove_dir(TDIR, rec=True)

_fcc_test = """00000
11111
55555
66666
77777
88888
88888
88888
99999"""

_fcc_final_expect = """00000
11111
22222
33333
44444
55555
66666
77777
88888
99999
00000"""

def test_file_data():
    # assert cache dir
    assert check_dir(GC)
    # make test dir
    make_dir(TDIR)
    mkfile_with_content(TDIR, TFILE, content=_fcc_test)
    cont = file_content(TDIR, TFILE, False)
    print("ffccccc")
    print(_fcc_test)
    print("contttt")
    print(cont)

test_file_data()
