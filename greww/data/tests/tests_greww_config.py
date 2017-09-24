import greww._config as CONFIG
from greww._envs import GREWW_CACHE, GREWW_CONFIG
from greww.data.basics import copy_file, remove_file

CFILE = 'cconfig.json'

def _generate_config_loader(c, p, fi):
    class claker(CONFIG.GConfigLoader):
        path = p
        f = fi
    claker.__name__ = c
    return claker

def test_gconfig_loader():
    # make class
    copy_file(GREWW_CONFIG, 'gconfig.json', GREWW_CACHE, CFILE)
    CL = _generate_config_loader('KAPPA', GREWW_CACHE, CFILE)
    # test class
    assert CL.__name__ == 'KAPPA'
    # test main source
    mainsource = tuple(CL.mainsource())
    assert (GREWW_CACHE, CFILE) == mainsource
    # test actual config
    assert CL.actual_config() == 'greww_config'
    # test configure
    CL.configure('machine_config')
    actual_config = CL.actual_config()
    assert CL.actual_config() == 'machine_config'
    #rebase
    CL.configure('greww_config')
    # add configs
    CL.add_config('kappa_config', 'kappapath', 'kappatype', True)
    data = CL.config_of(-1)
    assert data['path'] == 'kappapath'
    assert data['type'] == 'kappatype'
    assert CL.actual_config() == 'kappa_config'
    # rebase
    CL.configure('greww_config')
    # remove configure
    CL.remove_config('kappa_config')
    assert not ('kappa_config' in CL.all_configs())
    # clean up
    remove_file(GREWW_CACHE, CFILE)

def test_configuration():
    pass
