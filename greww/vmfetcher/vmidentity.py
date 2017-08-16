


def parse_machine_identity():
    pass

SQLL = {"host" : "127.0.0.1",
        "user" : "root",
        "password" : ""}

SQLC = {"use_pure" : True,
        "raise_on_warnings" : True}

class MachineIdentity(object):

    def __init__(self):
        pass

    def load(self, a):
        global SQLC, SQLL
        if a == "mysql.logs":
            return SQLL
        if a == "mysql.config":
            return SQLC

    @classmethod
    def _load(cls, cnf):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.load(cnf)
