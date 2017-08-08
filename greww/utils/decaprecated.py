# Decorate decaprecated functions
from .exceptions import DecaprecatedFunction

decaprecated = []

def decaprecateit(func):
    def pickle(*args, **kwargs):
        decaprecated.add(func)
        raise DecaprecatedFunction(func)
    return pickle

def get_decaprecated_functions(func):
    return decaprecated
