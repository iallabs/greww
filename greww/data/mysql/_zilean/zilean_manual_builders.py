from greww.data.mysql import (databases,
                              tables,
                              make_database,
                              make_table,
                              remove_database,
                              remove_table,
                              table_primary_start)

from greww.utils.exceptions import (NonAuthorizedMachine,
                                    NonAuthorizedLevel,
                                    FatalAssertion)

from greww.vmfetcher import MachineIdentity


def assert_zilean_core_databases():
    """
    Not Implemented
    """

    if MachineIdentity._load("identity.type") != "ZileanType":
        msg = """ Please make sure to use a ZileanMachine
        to assert it core databases. Other ways its not safe
        at all to make this kind of test possible from this
        package (greww). """
        raise NonAuthorizedMachine(msg)

    else:
        msg = """ Please make sure to use zilean-cli to make this
        kind of tests."""

    raise NonAuthorizedLevel(msg)

def build_zilean_core_database():
    """
    Not Implemented
    """
    msg = """ Can't build Zilean Core Database from an outsider
    package or non-zilean machine type """
    raise NonAuthorizedLevel()



def assert_machine_core_database():
    """
    Asserting machine database is called just to verifiy every single
    db is installed correctly.
    Return 1 if everything went good
    """

    core_database = MachineIdentity._load("mysql.core-database")
    authorisation = MachineIdentity._load("mysql.authorisations")
    # At this level authorisations are still ignored
    #FIXME: Having authorisation type doesnt stop you from doing anything
    #Zilean will just stop every unauthorised mouvement
    _db = databases()
    if not (core_database in _db):
        msg = "Damn it {0}".format(core_database)
        raise FatalAssertion(msg)
    return 1

def assert_zilean_machine_core_architecture():
    core_database = MachineIdentity._load("mysql.core-database")
    given_databases = MachineIdentity._load("mysql.databases")
    authorisation = MachineIdentity._load("mysql.authorisations")
    _db = databases()
    for i in given_databases:
        if not (i in _db):
            msg = "Damn it {0}".format(i)
            raise FatalAssertion(msg)
    _core_tables = tables(core_database)
    if not _core_tables:
        msg = "Damn it"
        raise FatalAssertion(msg)
    else:
        a = "machine_registred_moves"
        b = "machine_performance_history"
        c = "machine_traffic_history"
        if not (a in _core_tables or b in _core_tables or c in _core_tables):
            raise FatalAssertion()
    return 1

def build_machine_registred_moves():
    """
        Create a table that can hold all machine registred moves
        Probably going to be decorated
    """
    core_database = MachineIdentity._load("mysql.core-database")
    make_table(core_database,
               "machine_registred_moves",
               move_id="INT(10) NOT NULL AUTO_INCREMENT",
               caller="VARCHAR(30) NOT NULL",
               timed_at="timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
               function="VARCHAR(30) NOT NULL",
               arguments="JSON",
               out_put="JSON",
               run_time="INT(15)",
               success="BOOLEAN NOT NULL DEFAULT 1")
    table_primary_start(core_database,
                        "machine_registred_moves",
                        0)

#TODO
def build_machine_traffic_history():
    """
    Not Implemented
    """
    pass

#TODO
def build_machine_performance_history():
    """
    Not Impelemented
    """
    pass

def build_zilean_machine_database():
    pass
