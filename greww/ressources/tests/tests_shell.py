from greww.ressources.shell import Shell
from greww.data.basics import check_dir, list_dir
from greww._envs import GREWW_CACHE

DIR = "{0}/newdir__".format(GREWW_CACHE)
_lsg = "ls {0}".format(GREWW_CACHE)
_rmg = "rm -r {0}".format(DIR)
_un = "uname"
_mkdir = "mkdir {0}".format(DIR)
_stream = """(echo "import sys" ; echo "for r in range(10): print(r)") | python3"""


def test_all_executions():
    # simple execution
    Shell.execute(_mkdir)
    assert check_dir(DIR)
    # subprocess execution
    op = Shell.execute(_lsg, output=True, errors=True)
    assert op[0] == ['newdir__']
    assert not op[1]
    # subprocess no result no errors
    op = Shell.execute(_rmg, subprocess=True)
    assert not check_dir(DIR)
    # check err
    _, err = Shell._execute(_rmg)
    assert len(err) > 0

def test_check_output():
    # simple check
    x = Shell.check_output(_rmg)
    assert x == False
    x = Shell.check_output(_mkdir)
    assert x
    # subprocess check
    x = Shell.check_output(_rmg, True)
    assert x
    x = Shell.check_output(_rmg, True)
    assert not x

def test_catch_stream():
    Shell.catch_stream()

__all__ = [test_all_executions,
           test_check_output,
           test_catch_stream]
