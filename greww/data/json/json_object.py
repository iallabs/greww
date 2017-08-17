def jsonize_kwargs(*args, **kwargs):
    """
	Return a Json object that contain all data stored at args and kwargs
	"""
    keys = list(kwargs.keys())
    if not args:
        data = kwargs
    else:
        data = {
             "args" : list(args),
        }
        for k in keys:
            data[k] = kwargs[k]
    return data
