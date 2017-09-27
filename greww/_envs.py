import os

env = lambda var : os.environ[var]

try:
    GREWW_PATH = env('GREWW_PATH')
    GREWW_CACHE = env('GREWW_CACHE')
    GREWW_CONFIG = env('GREWW_CONFIG')
except:
    # no scop tests
    def _dispatch_path(fdir):
        fn, fd = '', ''
        bo = False
        for e in fdir[::-1]:
            if bo:
                fd += e
            elif e == '/':
                bo = True
            else:
                fn += e
        return fd[::-1], fn[::-1]
    _tmp = str(os.path.abspath(__file__))
    _tmp, _ = _dispatch_path(_tmp)
    _tmp, _ = _dispatch_path(_tmp)
    GREWW_PATH = _tmp
    GREWW_CACHE = _tmp + "/cache"
    GREWW_CONFIG = _tmp + "/pkg/config"

env = {
    'GREWW_PATH' : GREWW_PATH,
    'GREWW_CACHE' : GREWW_CACHE,
    'GREWW_CONFIG' : GREWW_CONFIG,
}
