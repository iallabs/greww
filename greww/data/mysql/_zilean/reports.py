from greww._config import Configuration as Config
from greww.data.mysql import add_element

GREWW_CONFIG = Config.load('greww.config')

GREWW_USE_PURE = GREWW_CONFIG['use_pure'] == 'true'
GREWW_CACHE_OPT = GREWW_CONFIG['cache_opt']
GREWW_TO_LIMIT = GREWW_CONFIG['time_out_limit']
GREWW_TO_LIMIT_R = GREWW_CONFIG['time_out_limit_on_request']

ZIELAN_CONFIG = Config.load('zilean.config')

ZILEAN_TYPE = ZILEAN_CONFIG['type']
ZILEAN_LOGS = ZILEAN_CONFIG['logs']
ZILEAN_CORE_DATABASE = ZILEAN_CONFIG['core_database']
ZILEAN_AUTHORISATION = ZILEAN_CONFIG['authorisation']
ZILEAN_AUTHORIZED_DATABASES = ZILEAN_CONFIG['authorized_databases']

ZILEAN_REPORTS = Config.load('zilean.reports')

ZILEAN_ACTIVE = ZILEAN_CONFIG['active'] == 'true'
ZILEAN_CALLER = ZILEAN_CONFIG['caller']
CACHE_ALL_MOVES = ZILEAN['cache_all_moves'] == 'true'
CACHE_FAILS = ZILEAN['cache_fails'] == 'true'

def _try_exec_with_time_out_limit(func, args, kwargs)

def machine_history():
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            if ZILEAN_ACTIVE:
                try:
                    func(*args, **kwargs)
                except:
                    pass
            else:
                return func(*args, **kwargs)

        return wrap_args
    return wrap_func
