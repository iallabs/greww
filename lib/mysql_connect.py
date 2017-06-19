import pymysql.cursors
from lib.mysql_logs.get_instance_logs


def mysql_connect(instance):
    host, port, user, password = get_instance_logs(instance)
    db = pymysql.connect(host=host,
                         user=user,
                         password=pw)
    return db
