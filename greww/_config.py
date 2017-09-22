from ._envs import GREWW_CONFIG
from .data.json import read_json, make_json
from .data.basics import remove_file
from .data.config import get_configurations, configuration_data
import skmvs as SK

GCF = "gconfig.json"

def _replace_json_file(d, f, nc):
    remove_file(d, f)
    make_json(d, f, from_data=nc)

class UnknownConfiguration(Exception):
    pass

class GrewwConfigLoader(object):
    """
    Greww Configurations
    """
    config_file = GREWW_CONFIG

    def __init__(self):
        self._data = self._load_configurations()
        self.version = self._data['greww_version']
        self.dependencies = self._data['babtu_dependencies']
        self.configuration = self._data['configuration']['active']
        self.configurations = self._data['configuration']['list']
        self.greww_config = self._data['configurations']['greww_config']
        self.machine_config = self._data['configurations']['machine_config']

    @staticmethod
    def _load_configurations():
        return read_json(GREWW_CONFIG, GCF)

    def _change_configuration_to(self, nc):
        if nc in self.configurations:
            self._data['configuration']['active'] = nc
            _replace_json_file(GREWW_CONFIG, GCF, self._data)
        else:
            raise UnknownConfiguration("")

    @classmethod
    def configure(cls, nc):
        obj = object.__new__(cls)
        obj.__init__()
        obj._change_configuration_to(nc)

    @classmethod
    def config_of(cls, config=None):
        obj = object.__new__(cls)
        obj.__init__()
        if config is None:
            config = obj.configuration
        return obj._data['configurations'][config]

    @classmethod
    def actual_config(cls):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.configuration


class Configuration(object):

    def __init__(self):
        self._path = SK.scan_expr(GrewwConfigLoader.config_of()['path'])
        self._configs = get_configurations(self._path)

    @classmethod
    def load(cls, config):
        obj = object.__new__(cls)
        obj.__init__()
        return configuration_data(obj._path, config)

    @classmethod
    def load_option(cls, config, option):
        return cls.load(config)[option]
