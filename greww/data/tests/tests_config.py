from greww.data.config import (get_configurations,
                               configuration_data,
                               get_options,
                               option_data,
                               set_configuration,
                               set_option,
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
    # make file
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

def tests_setters():
    set_configuration()
    set_option()
    make_configuration_file()

__all__ = [tests_parsers,
           tests_setters]
