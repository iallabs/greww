#

###################################
# Utils Exceptions

#TODO: make exception hierarchy


class CppModuleImport(Exception):
    def __init__(self, path):
        self.message = "Can't find path : {0}".format(path)
    pass

class CppFunctionImport(Exception):
    def __init__(self, func):
        self.message = "Can't find function : {0}".format(function)
    pass

class DefaultImportError(Exception):
    def __init__(self, value):
        self.message = "Can't import Default Value {0}".format(value)
    pass

class DecaprecatedFunction(Exception):
    pass

class MissingSettings(Exception):
    pass

class MissingMysqlLogs(MissingSettings):
    pass

class MissingCommand(Exception):
    pass
