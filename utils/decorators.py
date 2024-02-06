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

def Data_to_List(y,d,t):
    return_list = []
    data = open(f"./{y} Advent Calender/Day {d}/{t}.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list

def Dynamically_Nested_Lists(d,s,n):
    dictNum = f"{s}{n}"
    nestedList = []
    d[dictNum] = nestedList

    return d[dictNum]

def Dynamic_Dictionaries(d,s,n):
    dictNum = f"{s}{n}"
    dictionary = {}
    d[dictNum] = dictionary

    return d[dictNum]