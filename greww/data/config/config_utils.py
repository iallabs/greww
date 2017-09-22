import configparser
from greww.data.basics import (set_dir,
                               mkfile_with_content)

def get_configurations(full_path):
    """
    Get all configuration titles in target file
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config.sections()

def configuration_data(full_path, c):
    """
    Get all configuration options in a target file
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return dict(config[c])

def get_options(full_path, c):
    """
    Get options of configuration in a target file
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config[c].keys()

def option_data(full_path, c, o):
    """
    Get option value at configuration in a target file
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    return config[c][o]

def set_configuration():
    """
    Not Implemented
    """
    pass

def set_option():
    """
    NotImplemented
    """
    pass

def make_configuration_file():
    """
    Not Implemented
    """
    pass
