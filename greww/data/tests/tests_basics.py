import os

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
                               copy_file,
                               move_file,
                               add_line,
                               add_lines,
                               del_lines,
                               replace_lines,
                               file_size)

from greww._envs import GREWW_CACHE, GREWW_PATH

#GC = "/Users/ial-ah/GitHub/greww/cache"
#GP = "/Users/ial-ah/GitHub/greww"
GC, GP = GREWW_CACHE, GREWW_PATH


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
    assert 'tests' in d
    # set dir
    set_dir(GP)
    d = list_dir('cache')
    assert 'tests' in d
    set_dir(TDIR)
    # make dirs
    make_dir('testdir8')
    make_dir('testdir9')
    set_dir(GP)
    # find dir
    pd = find_dir(GP, 'testdir8')
    assert len(pd) == 1
    assert pd[0] == TDIR + '/testdir8'
    # remove dir
    remove_dir(TDIR + '/testdir8')
    # reove dir rec
    remove_dir(TDIR, True)
    pd = find_dir(GP, 'testdir8')
    assert len(pd) == 0
    # reconstrcut
    make_dir(TDIR)
    set_dir(TDIR)
    make_dir('testdir8')
    make_dir('testdir9')
    # make file
    make_file(TDIR, TFILE)
    # check file
    assert check_file(TDIR, TFILE)
    make_file(TDIR + '/testdir9', TFILE)
    # find_file
    pf = find_file(GP, TFILE)
    assert len(pf) == 2
    # copy_file
    copy_file(TDIR, TFILE, TDIR, 'copyofTFILE')
    assert check_file(TDIR, 'copyofTFILE')
    # check ct
    move_file(TDIR, 'copyofTFILE', TDIR, 'mvofTFILE')
    assert not check_file(TDIR, 'copyofTFILE')
    assert check_file(TDIR, 'mvofTFILE')
    # remove file
    remove_file(TDIR + '/testdir9', TFILE)

    pf = find_file(GP, TFILE)
    assert len(pf) == 1
    # remove
    remove_dir(TDIR, rec=True)

_fcc_test = """00000
11111
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
00000
"""

def test_file_data():
    # assert cache dir
    assert check_dir(GC)
    # make test dir
    make_dir(TDIR)
    mkfile_with_content(TDIR, TFILE, content=_fcc_test)
    # file content
    cont = file_content(TDIR, TFILE)
    # file lenght
    l = file_lenght(TDIR, TFILE)
    assert l == 6
    # add line
    add_line(TDIR, TFILE,
             line="00000", nline=10)
    l = file_lenght(TDIR, TFILE)
    assert l == 7
    # add lines
    add_lines(TDIR, TFILE,
              lines=["22222",
                     "33333",
                     "44444"],
               nline=2)
    # add lines
    add_lines(TDIR, TFILE,
              lines=["77777",
                     "66666",
                     "55555"],
              nline=5,
              inv=True)
    l = file_lenght(TDIR, TFILE)
    assert l == 13
    # del lines
    del_lines(TDIR, TFILE,
              nlines=[2,3],
              inv=True)
    l = file_lenght(TDIR, TFILE)
    assert l == 11
    cont = file_content(TDIR, TFILE, False)
    assert cont == _fcc_final_expect
    remove_dir(TDIR, rec=True)

test_file_data()

__all__ = [test_dir_file_basics,
           test_file_data]
