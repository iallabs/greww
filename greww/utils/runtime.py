import time

def calculate_run_time(func, loop=1):
    t1 = time.time()
    eval(func.__name__ + '()')
    t2 = time.time()
    return 'run in :'+ str(t2 - t1) + ' ms'

def runtime_eval(evl, loop=1):
	t1 = time.time()
	for i in range(0, loop):
		eval(evl)
	t2 = time.time()
	return 'run in :' + str(t2 - t1) + ' ms'


def timeit(func, active=True):
    def timed(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        if active:
            print('run time method* : ' + str(t2 - t1) + ' ms')
        return result
    return timed

# timedN
# run func with it args N time in order to detect unsual
# runtime differences
def timeitN(func, loop=1, report=True, active=True):
    def analyse(ln):
        an = []
        dn = []
        for i in range(0, len(ln) - 1):
            an += [ln[i + 1] - ln[i]]
        moy = sum(an) / len(an)
        for i in an:
            dn += [moy - i]
        return an, dn, moy

    def timedN(*args, **kwargs):
        t_records = [time.time()]
        for i in range(loop):
            result = func(*args, **kwargs)
            t_records += [time.time()]
        an, dn, moy = analyse(t_records)
        if active:
            print('run times for ' + str(loop) + ' times :', an)
            print('average run time ' + str(moy))
            print('diff run time from avg', an)
            print('total run time :' + sum(an))
        else:
            print('total run time :' + sum(an))
            print('avg ' + moy)
