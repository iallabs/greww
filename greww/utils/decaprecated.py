# Decorate decaprecated functions

decaprecated = set()

def is_decaprecated(func):
    def pickle(*args, **kwargs):
        decaprecated.add(func)
        return False
    pass

def get_decaprecated_functions(func):
    return decaprecated
