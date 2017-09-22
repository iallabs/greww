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

from greww._config import Configuration as Config

core_database = Config.laod_option('zilean.config', 'zilean_core_database')
authorisation = Config.load_option('zilean.config', 'zilean_authorisation')
given_databases = Config.load_option('zilean.config', 'zilean_authorized_databases')

zm_model = ["machine_registred_moves",
            "machine_performance_history",
            "machine_traffic_history"]

def assert_zilean_core_databases():
    """
    Not Implemented
    """
    if Config.load_option('zilean.config', 'zilean_type') != "main":
        msg = """ Please make sure to use a ZileanMachine
        to assert it core databases. Other ways its not safe
        at all to make this kind of test possible from this
        package (greww). """
        raise NonAuthorizedMachine(msg)

    else:
        msg = """ Please make sure to use zilean-cli/api to make this
        kind of tests."""
        raise NonAuthorizedLevel(msg)

def build_zilean_core_database():
    """
    Not Implemented
    """
    msg = """ Can't build Zilean Core Database from an outsider
    package or non-zilean machine type """
    raise NonAuthorizedLevel(msg)

def assert_machine_databases():
    """
    Asserting machine database is called just to verifiy every single
    db is installed correctly.
    Return 1 if everything went good
    """
    # At this level authorisations are still ignored
    #FIXME: Having authorisation type doesnt stop you from doing anything
    #Zilean will just stop every unauthorised mouvement
    _db = databases()
    t = core_database + given_databases
    for e in t:
        if not (e in _db):
            msg = "Damn it : {0}".format(core_database)
            raise FatalAssertion(msg)

def assert_zilean_machine_core_architecture():
    db = database()
    for i in given_databases:
        if not (i in db):
            msg = "Damn it {0}".format(i)
            raise FatalAssertion(msg)
    tb = tables(core_database)
    if not db:
        msg = "Damn it"
        raise FatalAssertion(msg)
    else:
        for i in zm_model:
            if not (i in tb):
                raise FatalAssertion()

def build_machine_registred_moves():
    """
        Create a table that can hold all machine registred moves
        Probably going to be decorated
    """
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
