from greww.shellenv.pyshell import execute_shell_command as esc
from greww.shellenv.shell import Shell
from greww.utils.filters import filter_iter as FI

_ls = "ls {0}"
_ls_la = "ls -la {0}"
_un = "uname"
_un_op = "uname {0}"
_mkdir = "mkdir {0}/{1}"
_rmdir = "rm -r {0}/{1}"



def test_esc_general():
    global _ls, _ls_la, _un
    dirs = esc(_ls.format("/"), rs=True)
    assert len(dirs) > 0
    system = esc(_un, rs=True)
    assert system

def test_esc_no_results():
    global _mkdir, _rmdir
    HOME = varenvs()["HOME"]
    dirs = esc(_ls.format(HOME), rs=True)
    bdirs = FI(dirs, c0)
    dir_test = "greww_test_dir"
    assert not (dir_test in bdirs)
    # Make test dir
    esc(_mkdir.format(HOME, dir_test))
    dirs = esc(_ls.format(HOME), rs=True)
    bdirs = FI(dirs, c0)
    assert dir_test in bdirs
    # Delete it
    esc(_rmdir.format(HOME, dir_test))
    dirs = esc(_ls.format(HOME), rs=True)
    bdirs = FI(dirs, c0)
    assert not (dir_test in bdirs)

def test_esc_streaming():
    pass

def test_shell_class_structure():
    pass

__all__ = [test_varenvs_,
           test_esc_general,
           test_esc_streaming,
           test_esc_no_results,
           test_shell_class_structure]
