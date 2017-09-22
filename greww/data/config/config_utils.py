import configparser
from greww.data.basics import (set_dir,
                               mkfile_with_content)

def get_configurations(full_path):
    """
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config.sections

def configuration_data(full_path, c):
    """
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return dict(config[c])

def get_options(full_path, c):
    """
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config[c].keys()

def option_data(full_path, c, o):
    """
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config[c][o]

def set_configuration():
    pass

def set_option():
    pass

def make_configuration_file():
    pass
