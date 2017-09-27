#

###################################
# Utils Exceptions

#TODO: make exception hierarchy


class MissingSettings(Exception):
    pass

class MissingMysqlLogs(MissingSettings):
    pass

class MissingCommand(Exception):
    pass

class FileNotFound(Exception):
    pass

class RejectedConnection(Exception):
    def __init__(self, logs=None, cnf=None):
        self.message = "Cannot connect to mysql-server using logs {0}".format(logs)

class BadConnector(Exception):
    def __init__(self, cnx):
        self.message = "Cannot use mysql-connector {0}".format(cnx)

class TimeoutError(Exception):
    pass

class NonAuthorizedMachine(Exception):
    pass

class NonAuthorizedLevel(Exception):
    pass

class FatalAssertion(Exception):
    pass

class WTF(Exception):
    pass

class LockedOption(Exception):
    pass

class NotImplementedAlgo(Exception):
    pass
