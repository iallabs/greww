import json

def create_json_file(name, secure=True):
    if secure:
        try:
            with open(name, 'w') as f:
        except:
            open(name, 'a').close()
    open(name, 'a').close()

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

def costum_db_architecture(name=None, tables):
    if name is None:
        err = ("Name is None")
    data = {
                name : tables
            }
    return data

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
