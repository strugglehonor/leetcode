import time
def func(f):
    def wrapper(f):
        time1 = time.time()
        f()
        time2 = time.time()
        return time2-time1
    return wrapper