# this is databases connector to python
import pymysql.cursors
import json
import argparse
import os

INSTANCES = 'instances.json'
ARCHITECTURES = 'hierarchy.json'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--logs')
    parser.add_argument('-a', '--architecture')
    parser.add_argument('-b', '--basearc')
    args = parser.parse_args()

    if args.logs:
        if args.logs == 'ALL':
            return get_all_logs()
        print(get_instance_logs(instance=args.logs))

    if args.architecture:
        if args.architecture == 'ALL':
            print(get_all_architectures())
        print(get_instance_logs(args.architecture))

    if args.basearc:
        print(get_db_architecture())

def get_instance_logs(instance=None):
    hostname = None
    port = None
    password = None
    username = None

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
    print(hostname, port, username, password)
    return (hostname, port, username, password)

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

def get_db_architecture():
    tables = []

    with open(ARCHITECTURES) as f:
        gen = json.loads(f.read())

    for entry in list(gen.keys()):
        if entry == architecture:
            dbs = entry
            for table in gen[entry]:
                tables += [table]

    return tables


if __name__ == "__main__":
    main()
