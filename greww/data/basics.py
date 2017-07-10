import os

####### directorys #######

def _stdir(directory):
    # set os directory
    os.chdir(directory)

def _ckdir(directory):
    # check directory
    return os.path.exists(directory)

def _mkdir(directory):
    # make directory
    if _ckdir(directory):
        #TODO: maybe an Exception here
        return 0
    os.makedirs(directory)

def _rmdir(directory, all=False):
    # remove directory
    if rec:
        import shutil
        shutil.rmtree(directory)
        return 0
    os.rmdir(directory)


######### files ##########

def _ckfile(directory, name):
    # check file
    return _ckdir(directory + name)

def _mkfile(directory, name, ext=None):
    # make file
    if _ckfile(directory, name):
        #TODO: maybe an Exception here
        return 0
    _file = open(directory + name, 'w').close()


def _rmfile(directory, name):
    # remove file
    if not _ckfile(directory, name):
        #TODO: Exception
        return
    os.remove(directory + name)

#####

def _mkfile_with_content(dir=None, name=None, ext=None, content=None):
    # make file with content
    pass

def _add_line_to_file(dir=None, name=None, line=None, nline=0, inv=False):
    pass

def _add_lines_to_file(dir=None, name=None, lines=None, nline=0, inv=False):
    pass

def _del_line_from_file(dir=None, name=None, line=None, nline=0, inv=False):
    pass

def _del_lines_from_file(dir=None, name=None, nlines=None, inv=False):
    pass

def _replace_lines_in_file(dir=None, name=None, nlines=None, lines=None, inv=False):
    pass
