import os
from greww.utils.filters import filter_app


def list_dir(directory):
    """
    List dir content
    """
    return os.listdir(directory)

def set_dir(directory):
    """
    Set os dir
    """
    os.chdir(directory)

def check_dir(directory):
    """
    Check Directory
    """
    return os.path.exists(directory)

def make_dir(directory):
    """
    Make Directory
    """
    os.makedirs(directory)


def remove_dir(directory, rec=False):
    """
    Remove directory
    Use rec to remove directory with it content
    """
    if rec:
        # NOTE: check if rec=False work for this case
        import shutil
        shutil.rmtree(directory)
    else:
        os.rmdir(directory)

def find_dir(directory, dir_name):
    """
    Find directory
    """
    r = []
    for root, dirs, files in os.walk(directory):
        if dir_name in dirs:
            r += [os.path.join(root, dir_name)]
    return r


######### files ##########

def check_file(directory, name):
    """
    Check file at directory
    """
    return check_dir(directory + "/" + name)

def make_file(directory, name=None, ext=None):
    """
    Make file at directory
    ext : Use ext to add extention
    """
    if ext:
        _file = open(directory + "/" + name + "." + ext, 'w').close()
    else:
        _file = open(directory + "/" + name, 'w').close()

def remove_file(directory, name):
    """
    Remove file at directory
    """
    os.remove(directory + "/" + name)

def find_file(directory, name):
    """
    Find file at directory
    """
    r = []
    for root, dirs, files in os.walk(directory):
        if name in files:
            r += [os.path.join(root, name)]
    return r

def mkfile_with_content(directory=None, name=None, ext=None, content=None):
    """
    Make file at directory
    ext : Use ext to add extention
    content : Use content to write content
    """
    if name is None:
        raise ValueError("Name can't be None")
    if ext:
        name += "." + ext
    set_dir(directory)
    with open(name, 'w') as f:
        if not content:
            return
        if type(content) == str:
            f.write(content)
        elif type(content) == list:
            for i in content:
                f.write(str(i) + "\n")
        else:
            f.write(content)

def replace_file(directory=None, name=None, new_content=None):
    """
    """
    raise NotImplemented("")

@filter_app(lambda x : x[:-1] if '\n' in x else x)
def _file_content_list(directory, name):
    set_dir(directory)
    with open(name, "r") as f:
        return f.readlines()

def file_content(directory=None, name=None, expand=True):
    """
    Return file content
    expand : Use expand to get a list of lines
    """
    if expand:
        return _file_content_list(directory, name)
    set_dir(directory)
    with open(name, "r") as f:
        return f.read()

def copy_file(directory, name, nd, nn):
    ct = file_content(directory, name)
    mkfile_with_content(nd, nn, content=ct)

def move_file(directory, name, nd, nn):
    copy_file(directory, name, nd, nn)
    remove_file(directory, name)

def file_lenght(directory=None, name=None):
    """
    Return File lenths ( Number of lines )
    """
    return len(file_content(directory, name, True))


def add_line(directory=None, name=None, line=None, nline=0, inv=False):
    """
    Add one line to file at directory
    nline : target line in file
    inv : Use inv to
    """
    # example
    # file.txt contain 4 lines and we want to add a line beetwin the 3rd and last
    # line wich means : push line 4 to line 5 ( and all lines after ) and add content
    # at the 4th line
    # _add_line_to_file(line="ajajajaj", nline=4)
    #IDEA: inv parameter (inverse) calculate lines from the end of the file
    # (add line to last line can be done with nline=0 and inv=True)
    if not check_file(directory, name):
        #TODO: Exception
        return
    content = file_content(directory, name, True)
    if inv:
        content = content[::-1]
    # insertion
    content.insert(nline, line)
    # recreate
    remove_file(directory, name)
    if inv:
        content = content[::-1]
    mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def add_lines(directory=None, name=None, lines=None, nline=0, inv=False, inv_writing=False):
    """
    Add list of lines to a file at directory
    nline : target line in file
    inv : Use inv to
    inv_writing : write lines[::-1] instead
    """
    if len(lines) == 1:
        return add_line(directory=directory,
                        name=name,
                        line=lines[0],
                        nline=nline,
                        inv=inv)
    if not check_file(directory, name):
        return
    # read
    content = file_content(directory, name, True)
    if inv:
        content = content[::-1]
    # insersion
    for line in lines:
        content.insert(nline, line)
        if inv_writing:
            nline -= 1
        else:
            nline += 1
    # recreate
    remove_file(directory, name)
    if inv:
        content = content[::-1]
    mkfile_with_content(directory=directory,
                        name=name,
                        content=content)

def del_lines(directory=None, name=None, nlines=None, inv=False):
    """
    Delete lines at nlines from file at directory
    """
    if not check_file(directory, name):
        return
    # read
    content = file_content(directory, name, True)
    if inv:
        content = content[::-1]
    i = 0
    def _incr_list(ln, incr):
        return [i+incr for i in ln]
    for line_i in range(len(nlines)):
        del content[nlines[line_i]]
        nlines = _incr_list(nlines, -1)
    # recreate
    remove_file(directory, name)
    if inv:
        content = content[::-1]
    mkfile_with_content(directory=directory,
                        name=name,
                        content=content)

def replace_lines(directory=None, name=None, nlines=None, lines=None, inv=False):
    #TODO:
    pass


def file_size():
    pass
