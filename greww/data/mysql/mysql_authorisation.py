

class MysqlAuthorisation(object):

    __slots__ = ["_rights",
                 "authorised_databases",
                 "authorised_tables"]

    def __new__(cls):
        pass

    def __init__(self):
        pass

    def _load_vm_config():
        pass

    def _load_authorisations():
        pass

    @property
    def rights(self):
        pass

    def have_rights(database=None, table=None):
        pass

    @classmethod
    def assert_rights(database=None, table=None):
        pass
