# this is databases connector to python
import pymysql.cursors
import json

INSTANCES = '/home/ubuntu/jsons/mysqlinst.json'
ARCHITECTURES = ''


def get_instance_logs(instance, instance_id=None, instance_name=None):
    hostname = None
    port = None
    password = None
    username = None
    instance = instance_id or instance_name or instance

    if not instance:
        err = ("No id or name given")
        raise NameError(err)

    with open(INSTANCES) as f:
        gen = json.loads(f.read())

    for entry in list(gen.keys()):
        if instance == entry:
            hostname = gen[entry]['host']
            port = gen[entry]['port']
            username = gen[entry]['username']
            password = gen[entry]['password']

    if hostname is None:
        err = ("Coulnd find instance")
        raise NameError(err)

    return hostname, port, username, password

def get_all_logs(ignore=None):
    instances = []
    logs = []

    with open(INSTANCES) as f:
        gen = json.loads(f.read())

    y = list(gen.keys())
    if ignore:
        y2 = []
        for e in y:
            if e in ignore:
                continue
            y2 += [e]
        y = y2
        del y2

    for entry in y:
        instances += [entry]
        logs += [(gen[entry]['host'],
                  gen[entry]['port'],
                  gen[entry]['username'],
                  gen[entry]['password'])]

    return instances, logs

def get_all_architectures():
    tables = []
    dbs = []

    with open(ARCHITECTURES) as f:
        gen = json.loads(f.read())

    for entry in list(gen.keys()):
        dbs += [entry]
        for table in gen[entry]:
            tables += [table]

    return tables, dbs

def get_db_architecture(architecture):
    tables = []

    with open(ARCHITECTURES) as f:
        gen = json.loads(f.read())

    for entry in list(gen.keys()):
        if entry == architecture:
            dbs = entry
            for table in gen[entry]:
                tables += [table]

    return tables
