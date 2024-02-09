

def Data_to_List(y,d,t):
    return_list = []
    data = open(f"./{y} Advent Calender/Day {d}/{t}.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


def List_to_Int(l):
    for _, i in enumerate(l):
        l[_] = int(l[_])
    
    return l

def Dynamically_Nested_Lists(d,s,n):
    listNum = f"{s}{n}"
    nestedList = []
    d[listNum] = nestedList

    return d[listNum]

def Dynamic_Dictionaries(d,s,n):# I think these are basically redundant and it's really the dynamic keys I was wanting
    dictNum = f"{s}{n}"
    dictionary = {}
    d[dictNum] = dictionary

    return d[dictNum]

def Dynamic_Keys(s,n):
    dictNum = f"{s}{n}"
    return dictNum