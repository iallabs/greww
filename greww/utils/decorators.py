# from nothing import nothing

def ClassDecorator(decorator=lambda x : x):
    """
    Decorate all method of classes with decorator
    """
    def decorate(cls):
        for attr in cls.__dict__: # there's propably a better way to do this
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate
