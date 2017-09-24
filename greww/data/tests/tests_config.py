from greww.data.config import (get_configurations,
                               configuration_data,
                               get_options,
                               option_data,
                               set_configuration,
                               set_option,
                               remove_configuration,
                               remove_option,
                               make_configuration_file)
from greww.data.basics import mkfile_with_content, remove_file
from greww._envs import GREWW_CACHE

__ini_file = "test.cfg"
__ini_sample = """
[del]
#

[test1]
kikou =
kika = jajaja
del = cc

[toutou]
ez = 1
"""

def tests_parsers():
    # make test file
    mkfile_with_content(GREWW_CACHE, __ini_file, content=__ini_sample)
    fp = "{0}/{1}".format(GREWW_CACHE, __ini_file)
    # get configs
    c = get_configurations(fp)
    assert 'test1' in c
    assert len(c) == 3
    # config content
    cd = configuration_data(fp, 'test1')
    assert len(cd.keys()) == 3
    assert 'cc' in cd.values()
    # get options
    o = get_options(fp, 'test1')
    assert len(o) == 3
    assert 'kikou' in o
    # get option value
    od = option_data(fp, 'test1', 'kika')
    assert od == 'jajaja'
    # remove test file
    remove_file(GREWW_CACHE, __ini_file)

def tests_setters():
    # make test file
    mkfile_with_content(GREWW_CACHE, __ini_file, content=__ini_sample)
    fp = "{0}/{1}".format(GREWW_CACHE, __ini_file)
    # set config
    nc = {'az' : '5', 'ez' : '2'}
    set_configuration(fp, 'toutou', **nc)
    d = get_configurations(fp)
    assert 'toutou' in d
    assert len(d) == 3
    _c = configuration_data(fp, 'toutou')
    assert _c == nc
    # set option
    set_option(fp, 'toutou', 'ez', '5')
    set_option(fp, 'toutou', 'kek', '6')
    o = get_options(fp, 'toutou')
    assert 'ez' in o
    assert 'kek' in o
    assert len(o) == 3
    assert option_data(fp, 'toutou', 'kek') == '6'
    assert option_data(fp, 'toutou', 'ez') == '5'
    # remove test file
    remove_file(GREWW_CACHE, __ini_file)

def tests_removers():
    # make test file
    mkfile_with_content(GREWW_CACHE, __ini_file, content=__ini_sample)
    fp = "{0}/{1}".format(GREWW_CACHE, __ini_file)
    # remove option
    remove_option(fp, 'test1', 'del')
    opts = get_options(fp, 'test1')
    assert len(opts) == 2
    assert not ('del' in opts)
    # remove configuration
    remove_configuration(fp, 'test1')
    cfgs = get_configurations(fp)
    assert len(cfgs) == 2
    assert not 'test1' in cfgs
    # remove test file
    remove_file(GREWW_CACHE, __ini_file)

def tests_makers():
    _cfs = ['alo', 'hello']
    _alo_d = {'ki' : 'da',
              're' : 'er'}
    _hello_d = {'ki' : 'ka',
                'ze' : '2',
                'zer' : '3'}
    fp = "{0}/{1}".format(GREWW_CACHE, __ini_file)
    make_configuration_file(fp, _cfs, [_alo_d, _hello_d])
    cfs = get_configurations(fp)
    assert len(cfs) == 2
    assert 'alo' in cfs and 'hello' in cfs
    opts = get_options(fp, 'alo')
    opts2 = get_options(fp, 'hello')
    assert len(opts) == 2 and len(opts2) == 3
    # remove test file
    remove_file(GREWW_CACHE, __ini_file)

__all__ = [tests_parsers,
           tests_setters,
           tests_removers,
           tests_makers]
