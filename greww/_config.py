from ._envs import GREWW_CONFIG
from .data.json import read_json, make_json, _replace_json
from .data.basics import remove_file
from .data.config import get_configurations, configuration_data
import skmvs as SK

GCF = "gconfig.json"


class UnknownConfiguration(Exception):
    pass

class ConfigurationAlreadyExists(Exception):
    pass

class CantRemoveUsingConfig(Exception):
    pass


class GConfigLoader(object):
    """
    Greww Configurations
    """
    config_file = GREWW_CONFIG

    def __init__(self, p=GREWW_CONFIG, f=GCF):
        self._data = self._load_configurations(p, f)
        self.version = self._data['greww_version']
        self.dependencies = self._data['babtu_dependencies']
        self.configuration = self._data['configuration']['active']
        self.configurations_list = self._data['configuration']['list']
        self.greww_config = self._data['configurations']['greww_config']
        self.machine_config = self._data['configurations']['machine_config']

    @staticmethod
    def _load_configurations(g, c):
        return read_json(g, c)

    def _change_configuration_to(self, nc):
        if nc in self.configurations_list:
            self._data['configuration']['active'] = nc
            _replace_json_file(GREWW_CONFIG, GCF, self._data)
        else:
            raise UnknownConfiguration("")

    def _new_configuration(self, name, path, t='__ini__'):
        if n in self.configurations_list:
            raise ConfigurationAlreadyExists("")
        else:
            self._data['configuration']['list'].append(name)
            cfg = {
                'path' : "{0}".format(path),
                'type' : "{0}".format(t),
            }
            self._data['configurations'].update({name : cfg})
            _replace_json_file(GREWW_CONFIG, GCF, self._data)

    def _remove_configuration(self, name):
        if n in self.configurations_list:
            self._data['configuration']['list'].remove(name)
            del self._data['configurations'][name]
            _replace_json_file(GREWW_CONFIG, GCF, self._data)
        else:
            UnknownConfiguration("")

    @classmethod
    def configure(cls, nc):
        obj = object.__new__(cls)
        obj.__init__()
        obj._change_configuration_to(nc)

    @classmethod
    def config_of(cls, config=None):
        obj = object.__new__(cls)
        obj.__init__()
        if config is None or config == -1:
            config = obj.configuration
        return obj._data['configurations'][config]

    @classmethod
    def actual_config(cls):
        obj = object.__new__(cls)
        obj.__init__()
        return obj.configuration

    @classmethod
    def add_config(cls, n, p, t, configure=False):
        obj = object.__new__(cls)
        obj.__init__()
        obj._new_configuration(n, p, t)
        if configure:
            obj._change_configuration_to(n)

    @classmethod
    def remove_config(cls, n):
        obj = object.__new__(cls)
        obj.__init__()
        if obj.configuration == n:
            raise CantRemoveUsingConfig("")
        else:
            obj._remove_configuration(n)

class Configuration(object):

    def __init__(self, path=None):
        self._path = path if path else SK.scan_expr(GConfigLoader.config_of(-1)['path'])
        self._configs = get_configurations(self._path)

    @classmethod
    def load(cls, config):
        obj = object.__new__(cls)
        obj.__init__()
        return configuration_data(obj._path, config)

    @classmethod
    def set(cls, config, new_config):
        obj = object.__new__(cls)
        obj.__init__()
        pass

    @classmethod
    def load_option(cls, config, option):
        return cls.load(config)[option]

    @classmethod
    def set_option(cls, config, option, value):
        obj = object.__new__(cls)
        obj.__init__()
        pass
