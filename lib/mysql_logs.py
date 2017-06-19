# this is databases connector to python
import pymysql.cursors
import json

INSTANCES = '/home/ubuntu/private/mysqlinst.json'
AUTH_FILE = '/Home/ubuntu/private/mysqlat.json'


def get_instance_logs(instance_id=None, instance_name=None):
    hostname = None
    port = None
    password = None
    username = None
    instance = instance_id or instance_name

    if not instance:
        err = ("No id or name given")
        raise NameError(err)

    with open(INSTANCES) as f:
        gen = json.loads(f.read())

    for entry in gen.iteritems():
        if instance == entry[0]:
            hostname = entry[1]['logs']['host']
            port = entry[1]['logs']['port']

    if hostname is None or port is None:
        err = ("Coulnd find hostname or port in INSTANCES")
        raise NameError(err)

    with open(AUTH_FILE) as f:
        gen = json.loads(f.read())

    for entry in gen.iteritems():
        if instance == entry[0]:
            username = entry[1]['username']
            password = entry[1]['password']

    if username is None or password is None:
        err = ("Couldnt find username or password in AUTH_FILE")
        raise NameError(err)

    return hostname, port, username, password

def get_all_logs(ignore=None):
    inst = []
    logs = []
    y = None

    with open(INSTANCES) as f:
        gen = json.loads(f.read())

    with open(AUTH_FILE) as f2:
        gen2 = json.loads(f2.read())

    for entry in gen.iteritems():
        inst += [(entry[0],
                  entry[1]['logs']['host'],
                  entry[1]['logs']['port'])]

    for instance in inst:
        _name = instance[0]
        for entry2 in gen2.iteritems():
            if _name == entry2[0]:
                y = instance + (entry2[1]['username'], entry2[1]['password'])
                logs += [y]

    return instance
