
GENERAL_SETTINGS = {
    "alias" : ["gs", "general", "GENERAL_SETTINGS", "general_settings"],
    "MAIN" : "greww",
    "PACKAGE" : "greww/greww",
    "C_PACKAGE" : "greww/greww/cgreww",
    "LIB_C_PACKAGE" : "greww/greww/cgreww/lib",
    "WORKING_DIRECTORY" : "greww/experience/op",
}


JSON_SETTINGS = {
    "alias" : ["js" , "json", "JSON_SETTINGS", "json_settings"],
    "PGREWW" : True,
    "CGREWW" : False,
    "FORCE_CGREWW" : False,
    "WORKING_DIRECTORY" : "greww/experience/op",
}


ALL = [GENERAL_SETTINGS,
       JSON_SETTINGS]



def _set_value(settings_name, **kws):
    global ALL
    for i in ALL:
        if settings_name in i["alias"]:
            break
    else:
        for k in list(kws.keys()):
            i[k] = kws[k]

def SETTINGS(module):
    global ALL
    if module == "ALL":
        return ALL
    for i in ALL:
        if module in i["alias"]:
            return i
    return


def deactivate_cgreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["CGREWW"] = False
            i["FORCE_CGREWW"] = False

def activate_cgreww(module):
    global ALL
    if module == "ALL":
        pass
    for i in ALL:
        if module in i["alias"]:
            i["CGREWW"] = True
            i["FORCE_CGREWW"] = True
