import os

####### directions #######

def _stdir(dir):
    # set os direction
    pass

def _ckdir(dir):
    # check direction
    pass

def _mkdir(dir):
    # make direction
    pass

def _rmdir(dir):
    # remove direction
    pass

######### files ##########

def _ckfile(dir, name):
    # check file
    pass

def _mkfile(dir, name, ext=None):
    # make file
    pass

def _rmfile(dir, name):
    # remove file
    pass

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
