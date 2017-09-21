SQLL = {"host" : "127.0.0.1",
        "user" : "root",
        "password" : ""}

SQLC = {"use_pure" : True,
        "raise_on_warnings" : True}

GREWW_WORKING_PATH = "/Users/ial/"

MACHINE_NAME = "kappa1"

class MachineIdentity(object):

    def __init__(self):
        pass

    def load(self, a):
        global SQLC, SQLL, MACHINE_NAME
        global GREWW_WORKING_PATH
        if a == "mysql.logs":
            return SQLL
        if a == "mysql.config":
            return SQLC
        if a == "GWP":
            return GREWW_WORKING_PATH
        if a == "identity.name":
            return MACHINE_NAME

    @classmethod
    def _load(cls, cnf):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.load(cnf)

class _Config(object):

    def __new__(self):
        pass

    def __init__(self):
        pass

    @property
    def _options(self):
        pass


class MachineConfig:

    def __new__(self):
        pass

    def __init__(self):
        pass

    @property
    def _configs(self):
        pass


def _find_machine_config_file():
    pass

def _parse_machine_config():
    pass

MachineConfiguration = _parse_machine_config()
