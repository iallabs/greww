from greww.shellenv import (varenvs,
                            unset_varenv,
                            export_varenv,
                            import_varenv)
from greww.shellenv.pyshell import (execute_shell_command,
                                    catch_shell_streaming)
from greww.shellenv.shell import Shell

_ls = "ls {0}"
_ls_la = "ls -la {0}"
_un = "uname"
_un_op = "uname {0}"
_mkdir_home = "mkdir $HOME/{0}"
_rmdir_home = "rm -rf $HOME/{0}"

esc = execute_shell_command

def test_esc_general():
    global _ls, _ls_la, _un
    dirs = esc(_ls.format("/"), rs=True)
    assert len(dirs) > 0
    system = esc(_un, rs=True)
    assert system

test_esc_general()

def test_esc_no_results():
    global _mkdir_home, _rmdir_home
    dirs = esc(_ls.format("$HOME"), shell=True, rs=True)
    dir_test = "greww_test_dir"
    assert not (dir_test in dirs)
    esc(_mkdir_home.format(dir_test), shell=True)
    dirs = esc(_ls.format("$HOME"), shell=True, rs=True)
    assert dir_test in dirs

test_esc_no_results()

css = catch_shell_streaming

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

def test_shell_class_structure():
    pass

__all__ = [test_esc_general,
           test_esc_streaming,
           test_varenvs,
           test_shell_class_structure]
