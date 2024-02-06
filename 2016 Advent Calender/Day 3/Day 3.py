Day_3 = "Squares With Three Sides"

possibleTriangles = 0

def file_to_list():
    return_list = []
    data = open("./2016 Advent Calender/Day 3/data.txt")
    #data = open("./2016 Advent Calender/Day 3/test.txt")
    for line in data:
        clean_data = filter(None,line.lower().split("\n"))
        return_list += clean_data

    return return_list


data = file_to_list()


def Check_Lengths(l):
    a = int(l[0])
    b = int(l[1])
    c = int(l[2])

    if a < (b+c):
        if b < (a+c):
            if c < (a+b):
                return True


for l in data:
    l = l.split()
    if Check_Lengths(l):
        possibleTriangles += 1

print(f"The answer to Part 1 is: {possibleTriangles}")


Part_2 = "Columns not Rows..."

possibleTriangles2 = 0

def Check_Lengths_2(x,y,z):
    
    if x < (y+z):
        if y < (x+z):
            if z < (x+y):
                return True


def Split_Triangles_2(j,k,l):
    return_value = 0

    j = j.split()
    k = k.split()
    l = l.split()

    a = int(j[0])
    b = int(k[0])
    c = int(l[0])
    if Check_Lengths_2(a,b,c):
        return_value += 1

    d = int(j[1])
    e = int(k[1])
    f = int(l[1])
    if Check_Lengths_2(d,e,f):
        return_value += 1

    g = int(j[2])
    h = int(k[2])
    i = int(l[2])
    if Check_Lengths_2(g,h,i):
        return_value += 1

    return return_value


for i, l in enumerate(data):
    x = i + 1
    if x % 3 == 0:
        possibleTriangles2 += Split_Triangles_2(data[i-2],data[i-1],l)


print(f"The answer to Part 2 is: {possibleTriangles2}")