from functools import wraps
from datetime import datetime


def time_it(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        start_time = datetime.now()
        ret = func(*args, **kwargs)
        end_time = datetime.now() - start_time
        print('func:%r took: %s' %
              (func.__name__, end_time))
        return ret
    return wrapped


