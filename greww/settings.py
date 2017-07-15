
GENERAL_SETTINGS = {
    "alias" : ["gs", "general", "GENERAL_SETTINGS", "general_settings"],
    "MAIN" : "greww",
    "PACKAGE" : "greww/greww",
    "C_PACKAGE" : "greww/greww/cgreww",
    "LIB_C_PACKAGE" : "greww/greww/cgreww/lib",
    "WORKING_DIRECTORY" : "greww/experience/op",
}

ENVIRENEMENT = {
    "Active" : "True",
    "CGreww" : "False",
    "PyGreww" : "True",
}


JSON_SETTINGS = {
    "alias" : ["js" , "json", "JSON_SETTINGS", "json_settings", "json_utils", "json_object", "json_tests"],
    "sopath" : "greww/greww/cgreww/lib/json_utils.so",
    "WORKING_DIRECTORY" : "/home/ubuntu/greww/experience/op",
    "ENVIRENEMENT" : ENVIRENEMENT,
}


MYSQL_SETTINGS = {
    "alias" : ["sql", "mysql", "MYSQL_SETTINGS", "mysql_settings", "mysql_utils", "mysql_search", "mysql_tests"],
    "sopath" : "greww/greww/cgreww/lib/mysql_utils.so",
    "WORKING_DIRECTORY" : "greww/experience/op",
    "MYSQL_LOGS" : ("localhost", "", "root", "uehMLMRw"),
    "ENVIRENEMENT" : ENVIRENEMENT,
}




ALL = [GENERAL_SETTINGS,
       JSON_SETTINGS,
       MYSQL_SETTINGS]


def _set_value(settings_name, **kws):
    global ALL
    for i in ALL:
        if settings_name in i["alias"]:
            break
    else:
        for k in list(kws.keys()):
            i[k] = kws[k]

def SETTINGS(module, target):
    global ALL
    if module == "ALL":
        return ALL
    for i in ALL:
        if target == "ALL":
            if module in i["alias"]:
                return i
    return


def deactivate_cgreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["ENVIRENEMENT"]["CGreww"] = False

def activate_cgreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["ENVIRENEMENT"]["CGreww"] = True

def deactivate_pygreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["ENVIRENEMENT"]["PyGreww"] = False

def activate_pygreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["ENVIRENEMENT"]["PyGreww"] = True
