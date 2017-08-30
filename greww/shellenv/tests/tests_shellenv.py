from greww.shellenv import (unset_varenv,
                            export_varenv,
                            import_varenv,
                            execute_shell_command)
from greww.shellenv.shell import Shell

def test_esc_general():
    pass

def test_esc_streaming():
    pass

def test_varenvs():
    pass

def test_shell_class_structure():
    pass

_ls = "ls {0}"
_ls = "ls -la {0}"
_top = "top"

__all__ = [test_esc_general,
           test_esc_streaming,
           test_varenvs,
           test_shell_class_structure]
