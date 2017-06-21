import json
import argparse
from lib.mysql_logs import INSTANCES, ARCHITECTURES

import os
default='/Users/IAL/Documents/GitHub/mysql_utils'

def set_direction(direction):
    os.chdir(direction)

set_direction(direction=default)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', type=str)
    parser.add_argument('-a', '--add', type=tuple)
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument('-t', '--type', type=str)
    args = parser.parse_args()

    if args.new:
        if args.type == 'json':
            create_json_file(args.new)
        else:
            err = ('type not implemented')
            raise Exception(err)
        create_file(args.new, secure=True)

    if args.add:
        if args.file:
            if args.type == 'logs':
                add_element_tojson(args.file, costum_instance_data(args.add))
            if args.type == 'arc':
                add_element_tojson(args.file, costum_db_architecture(args.add))


def create_file(name, secure=True):
    if secure:
        try:
            with open(name, 'w') as f:
                err = ('file already exist')
                raise Exception(err)
        except:
            open(name, 'a').close()
    open(name, 'a').close()

def create_json_file(name, secure=True):
    name = name + '.json'
    create_file(name, secure=secure)

def create_and_dump(name, data):
    create_json_file(name)
    write_json(name, data)

def costum_instance_data(name=None, host=None, port=None, username=None, password=None):
    if name is None:
        err = ("Name is None")
        raise NameError(err)
    data = {
                name : {
                            'host' : host,
                            'port' : port,
                            'username' : username,
                            'password' : password
                        }
            }
    return data

def costum_db_architecture(name=None, tables=None):
    if name is None:
        err = ("Name is None")
    data = {
                name : tables
            }
    return data

def costum_slaver(name=None, ip=None, pem=None):
    pass

def one_costum(forr=None, **kwargs):
    if not forr:
        return
    if not kwargs:
        return
    keys = list(kwargs.keys())
    forr = list(forr)
    if not _include_list(keys, forr):
        return
    res = {}
    for key in forr:
        res[key] = kwarg[key]
    return res



def add_element_tojson(element, _file):
    try:
        with open(_file) as f:
            data = json.load(f)
            data.update(element)
        with open(_file, 'w') as f:
            json.dump(data, f)
    except:
        with open(_file, 'w') as f:
            data = element
            json.dump(data, f)



if __name__ == "__main__":
    main()

# instance
#
# sample
"""
{
    'IAL-Central' : {
                        'host' : 'localhost',
                        'port' : '',
                     }

     'LicapyWBS' :  {
                         'host' : 'localhost',
                         'port' : '',
                    }
}
"""

# architecture sample

"""
{
    "IALCentraldb" : {
                            "ipdata" : ["name", "ip", "authority"]
                            "users" : ["username", "name", "email", "password"]
                            "slaves" : ["slave", "ip", "state", "pem"]
                            "stats" : ["date", "records"]
                            "logs" : ["date, ""username"]
                            "history" : ["date", "username", "command"]
                     },
    "IALBackends" :  {
                            "Backends" : ["Backendsbash"]
                     }
}
"""
