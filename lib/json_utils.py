import json
import argparse
from lib.mysql_logs import INSTANCES, ARCHITECTURES

import os

# default='/Users/IAL/Documents/GitHub/mysql_utils'
default = '/home/ubuntu/data'


def set_direction(direction):
    os.chdir(direction)

set_direction(direction=default)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', type=str)
    parser.add_argument('-a', '--add', type=tuple)
    parser.add_argument('-p', '--path', type=str, default='/home/ubuntu/data')
    parser.add_argument('-f', '--file', type=str)
    args = parser.parse_args()

    if args.new:
        if args.type == 'json':
            create_json_file(args.new, direction=args.path)
        else:
            err = ('type not implemented')
            raise Exception(err)
        create_file(args.new, direction=args.path, secure=True)

    if args.add:
        if args.file:
            add_element_tojson(args.file, costum_instance(args.add))



def create_file(name, direction=default, secure=True):
    set_direction(direction)
    if secure:
        try:
            with open(name, 'w') as f:
                err = ('file already exist')
                raise Exception(err)
        except:
            open(name, 'a').close()
    open(name, 'a').close()


def create_json_file(name, direction=default, secure=True):
    set_direction(direction)
    name = name + '.json'
    create_file(name, secure=secure)


def add_element_tojson(element, _file , direction):
    set_direction(direction)
    try:
        with open(_file) as f:
            data = json.load(f)
            data.update(element)
        with open(_file, 'w') as f:
            json.dump(data, f)
    except:
        err = 'file dosent exist'
        raise Exception(err)


def create_and_dump(name, direction=default, data=None):
    set_direction(direction)
    create_json_file(name)
    if data:
        add_element_tojson(name, data)

def costum_instance(name=None,
                    idd=0,
                    kind="",
                    host="",
                    port="",
                    user="",
                    password="",
                    ip="",
                    private="",
                    pem="",
                    dns="",
                    hierarchy=None
                    slaves=None):
    if not name:
        raise Exception('Name is none')

    data = {
              "instance" : name,
              "id" : idd,
              "type" : kind,
              "mysqllogs" : {
                            "host" : host,
                            "port" : port,
                            "user" : user,
                            "password" : password
                         },
              "sshlogs" : {
                             "ip" : ip,
                             "private" : private,
                             "dns" : dns,
                             "pem" : pem
                          },
              "hierarchy" : hierarchy
              "slaves" : slaves
    }

    if slaves is None:
        del data["slaves"]
    if hierarchy is None:
        del data["hierarchy"]

    return data


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
        if key in keys:
            res[key] = kwarg[key]
        else:
            res[key] = ""
    return res



if __name__ == "__main__":
    main()

# instance
#
# sample
"""
[
    {
        "instance" : "IAL-Central",
        "id" : "0000",
        "type" : "",
        "mysqllogs" : {
                         "host" : "",
                         "port" : "",
                         "user" : "",
                         "password" : ""
        },
        "sshlogs" : {
                        "ip" : "",
                        "private" : "",
                        "dns" : "",
                        "pem" : ""
        },
        "hierarchy" : {
                         "ipdata" : ["name", "ip", "authority"],
                         "users" : ["username", "name", "email", "password"],
                         "slaves" : ["slave", "ip", "state", "pem"],
                         "stats" : ["date", "records"],
                         "logs" : ["date, ""username"],
                         "history" : ["date", "username", "command"]
        }
        "slaves" : []
    }
]
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
