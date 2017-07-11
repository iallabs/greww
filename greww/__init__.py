from .utils.cboost import call_cpp_function

GetSettings = call_cpp_function(GetSettings,
                                path="settings.so",
                                int_put="str",
                                out_put="str")


# General settings
"""
GENERAL_SETTINGS = {
    WORKING_DIRECTORY = 1,
    OUTPUT_DIRECTORY = 1,
    INPUT_DIRECTORY = 1
}

JSON_SETTINGS =

MYSQL_SETTINGS = {
    HOST = 1,
    PORT = 1,
    USER = 1,
    PASSWORD = 1
}

SERVER_SETTINGS = {}
"""
