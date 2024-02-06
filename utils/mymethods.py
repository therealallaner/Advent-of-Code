

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