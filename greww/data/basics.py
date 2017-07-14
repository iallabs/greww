import os

####### directorys #######

#TODO: import settings

DEFAULT = "/Users"
#/home/ubuntu/greww


def lsdir(directory):
    return os.listdir(directory)

def stdir(directory):
    # set os directory
    os.chdir(directory)

def ckdir(directory):
    # check directory
    return os.path.exists(directory)

def mkdir(directory):
    # make directory
    if _ckdir(directory):
        #TODO: maybe an Exception here
        return 0
    os.makedirs(directory)

def rmdir(directory, all=False):
    # remove directory
    if rec:
        import shutil
        shutil.rmtree(directory)
        return 0
    os.rmdir(directory)


######### files ##########

def ckfile(directory, name):
    # check file
    return _ckdir(directory + name)

def mkfile(directory, name, ext=None):
    # make file
    if _ckfile(directory, name):
        #TODO: maybe an Exception here
        return 0
    _file = open(directory + name, 'w').close()


def rmfile(directory, name):
    # remove file
    if not _ckfile(directory, name):
        #TODO: Exception
        return
    os.remove(directory + name)

#####


def mkfile(directory=None, name=None, ext=None):
    pass


def mkfile_with_content(directory=None, name=None, ext=None, content=None):
    # make file with content
    if directory is None or name is None:
        #TODO: execption
        return 0
    if ext:
        name += ext
    if not _ckdir(directory):
        #TODO: execption
        return 0
    if _ckfile(directory, name):
        #TODO: execption
        return 0

    import collections.Iterable
    _mkfile(directory, name)

    if not content:
        return

    _stdir(directory)
    with open(name, 'w') as f:
        if isinstance(theElement, collections.Iterable):
            for i in content:
                f.write(i)
        else:
            f.write(content)

def file_lenght(directory=None, name=None):
    if directory is None or name is None:
        #TODO: execption
        return 0
    if _ckfile(directory, name):
        #TODO: execption
        return 0
    with open(name, 'w') as f:
        return len(f.readlines())


def add_line_to_file(directory=None, name=None, line=None, nline=0, inv=False):
    # example
    # file.txt contain 4 lines and we want to add a line beetwin the 3rd and last
    # line wich means : push line 4 to line 5 ( and all lines after ) and add content
    # at the 4th line
    # _add_line_to_file(line="ajajajaj", nline=4)
    #IDEA: inv parameter (inverse) calculate lines from the end of the file
    # (add line to last line can be done with nline=0 and inv=True)
    if not _ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = _file_lenght(directory, name) - nline
    # read
    _stdir(directory)
    with open(name, 'r') as f:
        content = f.readlines()
    # insertion
    content.insert(nline, line)
    # recreate
    _rmfile(directory, name)
    _mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def add_lines_to_file(directory=None, name=None, lines=None, nline=0, inv=False, inv_writing=False):
    if not _ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = _file_lenght(directory, name) - nline
    # read
    _stdir(directory)
    with open(name, 'r') as f:
        content = f.readlines()
    # insersion
    for line in lines:
        content.insert(nline, line)
        if inv_writing:
            nline -= 1
        else:
            nline += 1
    # recreate
    _rmfile(directory, name)
    _mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def del_lines_from_file(directory=None, name=None, nlines=None, inv=False):
    if not _ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = _file_lenght(directory, name) - nline
    # read
    _stdir(directory)
    with open(name, 'r') as f:
        content = f.readlines()

    #TODO: to functions module
    def _incr_list(ln, incr):
        return [i+incr for i in ln]
    i = 0
    while nlines:
        del content[nlines[i]]
        nlines = _incr_list(nlines, -1)
        i += 1
    # recreate
    _rmfile(directory, name)
    _mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def replace_lines_in_file(directory=None, name=None, nlines=None, lines=None, inv=False):
    #TODO:
    pass

def this_file_name():
    print(__name__)
