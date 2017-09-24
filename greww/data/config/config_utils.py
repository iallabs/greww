import configparser
from greww.data.basics import make_file, remove_file

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

def _dispatch_path(p):
    _file = ''
    _path = ''
    slash_found = False
    for i in p[::-1]:
        if i == '/' and not slash_found:
            slash_found = True
        elif slash_found:
            _file += i
        else:
            _path += i
    return _file[::-1], _path[::-1]

def set_configuration(full_path, c, **kwargs):
    """
    Set configuration c with kwargs
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    config[c] = kwargs
    # recreate
    remove_file(*_dispatch_path(full_path))
    f = open(full_path, 'w')
    config.write(f)
    f.close()

def set_option(full_path, c, o, value):
    """
    Set option o with value v at configuration c
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    config[c][o] = value
    # recreate
    remove_file(*_dispatch_path(full_path))
    f = open(full_path, 'w')
    config.write(f)
    f.close()

def remove_configuration(full_path, c):
    """
    Remove all configuration c with it content
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    del config[c]
    # recreate
    remove_file(*_dispatch_path(full_path))
    f = open(full_path, 'w')
    config.write(f)
    f.close()

def remove_option(full_path, c, o):
    """
    Remove option o from configuration c
    """
    config = configparser.ConfigParser()
    config.read(full_path)
    del config[c][o]
    # recreate
    remove_file(*_dispatch_path(full_path))
    f = open(full_path, 'w')
    config.write(f)
    f.close()

def make_configuration_file(full_path, configurations, dictlist):
    """
    Make configuration file as format
    [configuration[0]]
    dictlist[0]

    [configuration[1]]
    dictlist[1]

    ...
    """
    make_file(*_dispatch_path(full_path))
    l = len(configurations)
    for i in range(l):
        set_configuration(full_path, configurations[i], **dictlist[i])
