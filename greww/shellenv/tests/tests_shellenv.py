from greww.shellenv import (varenvs,
                            unset_varenv,
                            export_varenv,
                            import_varenv)
from greww.shellenv.pyshell import execute_shell_command as esc
from greww.shellenv.shell import Shell
from greww.filters.dynamic_filters import filter_iter as FI
from greww.utils.strbin import convert_bin_to_str as c0

_ls = "ls {0}"
_ls_la = "ls -la {0}"
_un = "uname"
_un_op = "uname {0}"
_mkdir = "mkdir {0}/{1}"
_rmdir = "rm -r {0}/{1}"

def test_varenvs():
    env_dict = varenvs()
    keys = env_dict.keys()
    # Verify those variables are declared in shell
    # Those variable always exist on any type of unix
    assert "HOME" in keys \
           and "PWD" in keys \
           and "USER" in keys \
           and "OLDPWD" in keys \
           and "SHELL" in keys \

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

def test_varenvs():
    ve = varenvs().keys()
    assert "HOME" in ve
    assert "USER" in ve
    assert "SHELL" in ve
    vhome = import_varenv("HOME")
    assert vhome
    vuser = import_varenv("USER")
    assert vuser
    vshell = import_varenv("SHELL")
    assert vshell == "/bin/bash"
    _test_ve = "TESTVAR_0"
    _test_value = "NONE-LOL"
    export_varenv(_test_ve, _test_value)
    ve = varenvs()
    value = import_varenv(_test_ve)
    assert value == _test_value
    assert ve[_test_ve] == _test_value
    unset_varenv(_test_ve)
    ve = varenvs()
    assert not (_test_ve in ve.keys())

def test_shell_class_structure():
    pass

__all__ = [test_esc_general,
           test_esc_streaming,
           test_varenvs,
           test_shell_class_structure]
