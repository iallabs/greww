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
    if ckdir(directory):
        #TODO: maybe an Exception here
        return 0
    os.makedirs(directory)

def rmdir(directory, all=False, rec=False):
    # remove directory
    if rec:
        import shutil
        shutil.rmtree(directory)
        return 0
    os.rmdir(directory)


######### files ##########

def ckfile(directory, name):
    # check file
    return ckdir(directory + "/" + name)

def mkfile(directory, name=None, ext=None):
    # make file
    if ckfile(directory, name):
        #TODO: maybe an Exception here
        return 0
    if ext:
        _file = open(directory + "/" + name + "." + ext, 'w').close()
    else:
        _file = open(directory + "/" + name, 'w').close()

def rmfile(directory, name):
    # remove file
    if not ckfile(directory, name):
        #TODO: Exception
        return
    os.remove(directory + "/" + name)

####


def mkfile_with_content(directory=None, name=None, ext=None, content=None):
    # make file with content
    if directory is None or name is None:
        #TODO: execption
        return 0
    if ext:
        name += "." + ext
    if not ckdir(directory):
        #TODO: execption
        return 0
    if ckfile(directory, name):
        #TODO: execption
        return 0

    stdir(directory)
    with open(name, 'w') as f:
        if not content:
            return
        if type(content) == str:
            f.write(content)
        elif type(content) == list:
            for i in content:
                f.write(i + "\n")
        else:
            f.write(content)


def file_content(directory=None, name=None, expand=True):
    ckfile(directory, name)
    stdir(directory)
    with open(name, "r") as f:
        if expand:
            return f.readlines()
        else:
            return f.read()


def file_lenght(directory=None, name=None):
    if directory is None or name is None:
        #TODO: execption
        return 0
    if not ckfile(directory, name):
        #TODO: execption
        return -1
    stdir(directory)
    with open(name, 'r') as f:
        return len(f.readlines())


def add_line_to_file(directory=None, name=None, line=None, nline=0, inv=False):
    # example
    # file.txt contain 4 lines and we want to add a line beetwin the 3rd and last
    # line wich means : push line 4 to line 5 ( and all lines after ) and add content
    # at the 4th line
    # _add_line_to_file(line="ajajajaj", nline=4)
    #IDEA: inv parameter (inverse) calculate lines from the end of the file
    # (add line to last line can be done with nline=0 and inv=True)
    if not ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = file_lenght(directory, name) - nline
    # read
    stdir(directory)
    with open(name, 'r') as f:
        content = f.readlines()
    # insertion
    content.insert(nline, line)
    # recreate
    rmfile(directory, name)
    mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def add_lines_to_file(directory=None, name=None, lines=None, nline=0, inv=False, inv_writing=False):
    if not ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = file_lenght(directory, name) - nline
    # read
    stdir(directory)
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
    rmfile(directory, name)
    mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def del_lines_from_file(directory=None, name=None, nlines=None, inv=False):
    if not ckfile(directory, name):
        #TODO: Exception
        return
    if inv:
        #XXX: Not sure about this
        nline = file_lenght(directory, name) - nline
    # read
    stdir(directory)
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
    rmfile(directory, name)
    mkfile_with_content(directory=directory,
                         name=name,
                         content=content)


def replace_lines_in_file(directory=None, name=None, nlines=None, lines=None, inv=False):
    #TODO:
    pass


def file_size():
    pass
