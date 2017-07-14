MAIN="greww"
PACKAGE="greww/greww"
C_PACKAGE="greww/greww/cgreww"
LIB_C_PACKAGE="greww/greww/cgreww/lib"
WORKING_DIRECTORY="greww/experience/op"
C = False



def _ignore_c_settings():
    C = False

def _make_c_settings():
    C = True

def c_settings():
    return C
