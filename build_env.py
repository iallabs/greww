import os
import skmvs as SK

GP = os.environ['GREWW_PATH']
GV = os.environ['GREWW_VERSION']
GC = os.environ['GREWW_CACHE']
GG = os.environ['GREWW_CONFIG']

def build_env():
    SK.store_value('GREWW_PATH', GP, db='paths', force=True)
    SK.store_value('GREWW_CACHE', GC, db='paths', force=True)
    SK.store_value('GREWW_CONFIG', GG, db='paths', force=True)
    SK.store_value('GREWW_VERSION', GV, db='main', force=True)
    SK.store_value("greww_paths_stored", True, db="main", force=True)

if __name__ == "__main__":
    build_env()
