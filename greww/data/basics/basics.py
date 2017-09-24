from ._basics import (list_dir,
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
                      copy_file,
                      move_file,
                      file_lenght,
                      add_line,
                      add_lines,
                      del_lines,
                      replace_lines,
                      file_size)

DirApiFunctions = {"list_dir" : list_dir,
                   "set_dir" : set_dir,
                   "check_dir" : check_dir,
                   "make_dir" : make_dir,
                   "remove_dir" : remove_dir}

FileApiFunctions = {"find_dir" : check_file,
                    "find_file" : find_file,
                    "make_file" : make_file,
                    "check_file" : check_file,
                    "remove_file" : remove_file,
                    "move_file" : move_file,
                    "copy_file" : copy_file,
                    "mkfile_with_content" : mkfile_with_content,
                    "file_lenght" : file_lenght,
                    "file_content" : file_content,
                    "add_line" : add_line,
                    "add_lines" : add_lines,
                    "del_lines" : del_lines,
                    "replace_lines" : replace_lines,
                    "file_size" : file_size}


class _GrewwDirectory(object):
    __slots__ = [method for method in DirApiFunctions.keys()]
    def __new__(cls):
        obj = object.__new__(cls)
        for method, func in DirApiFunctions.items():
            setattr(obj,
                    method,
                    func)
        return obj

GrewwDirectory = _GrewwDirectory()

class _GrewwFile(object):
    __slots__ = [method for method in FileApiFunctions.keys()]
    def __new__(cls):
        obj = object.__new__(cls)
        for method, func in FileApiFunctions.items():
            setattr(obj,
                    method,
                    func)
        return obj

GrewwFile = _GrewwFile()
