
# to import default settings use
# import files settings use import to the closest  __init__ file
# for example MYSQLDEFAULTROOT should be at greww/data/mysql/__init__.py

import greww as GREWW
import greww.utils as UTILS
import greww.data as DATA
import greww.data.json as JSON
import greww.data.mysql as MYSQL
import greww.service as SERVICE

from .exceptions import DefaultImportError

default = {
    "greww" : GREWW,
    "utils" : UTILS,
    "json" : JSON,
    "mysql" : MYSQL,
    "data" : DATA,
    "service" : SERVICE,
}

def import_default_value(module, name=None, names=None):
    if name is None and names is None:
        raise DefaultImportError()
    global default
    if name:
        return getattr(default[module], name)
    elif names:
        return [getattr(default[module], i) for i in names]
