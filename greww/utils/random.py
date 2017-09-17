import random

MAX_GRAVITY = 100

def generate_random_float(a, b, gravity=50):
    global MAX_GRAVITY
    if gravity in [0, 100]:
        raise Exception("")
    rand = random.random(a, b)

def generate_random_boolean(gravity=50):
    global MAX_GRAVITY
    if gravity in [0, 100]:
        raise Exception("")
    pass

def pop_random(ln, gravity=None):
    global MAX_GRAVITY
    if gravity in [0, 100]:
        raise Exception("")
    pass
