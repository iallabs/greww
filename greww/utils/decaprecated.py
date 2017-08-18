# Decorate decaprecated functions
from .exceptions import DecaprecatedFunction

decaprecated = []

def decaprecateit(func):
    def pickle(*args, **kwargs):
        global decaprecated
        decaprecated.append(func)
        raise DecaprecatedFunction(func)
    return pickle

def get_decaprecated_functions(func):
    global decaprecated
    return decaprecated
