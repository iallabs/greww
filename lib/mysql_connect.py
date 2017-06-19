import pymysql.cursors
from lib.mysql_logs.get_instance_logs
THIS_INSTANCE = ''

def mysql_connect(instance=None, local=True):
    if local:
        instance = THIS_INSTANCE
    elif instance is None:
        err = ('No instance given')
        raise NameError(err)
    host, port, user, password = get_instance_logs(instance)
    db = pymysql.connect(host=host,
                         user=user,
                         password=pw)
    return db
