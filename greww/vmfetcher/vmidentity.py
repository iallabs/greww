

def parse_machine_identity():
    pass

SQLL = {"host" : "127.0.0.1",
        "user" : "root",
        "password" : ""}

SQLC = {"use_pure" : True,
        "raise_on_warnings" : True}

GREWW_WORKING_PATH = "/Users/ial/"

class MachineIdentity(object):

    def __init__(self):
        pass

    def load(self, a):
        global SQLC, SQLL
        global GREWW_WORKING_PATH
        if a == "mysql.logs":
            return SQLL
        if a == "mysql.config":
            return SQLC
        if a == "GWP":
            return GREWW_WORKING_PATH

    @classmethod
    def _load(cls, cnf):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.load(cnf)
