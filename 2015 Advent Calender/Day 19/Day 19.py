from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_18 = "Medicine for Rudolph"


data = Data_to_List(2015,19,"data")
m1 = Data_to_List(2015,19,"m1")

test = Data_to_List(2015,19,"test")
m2 = Data_to_List(2015,19,"m2")


def Convert_Replacements(d):
    newList = []
    for l in d:
        l = l.split()
        newList.append(l)
    return newList
        

def Check_Singles(m,r):
    starterMolecule = str(m[0])

    molecules = []
    stringPast = ""
    stringFuture = ""

    for x, i in enumerate(m[0]):
        stringFuture = str(m[0][x+1:])
        for l in r:
            if i == l[0]:
                mol = (stringPast + l[2] + stringFuture)

                if mol not in molecules:
                    molecules.append(mol)

        stringPast += i

    return molecules


def Check_Doubles(m,r):
    starterMolecule = str(m[0])

    molecules = []
    stringPast = ""
    stringFuture = ""

    for x, i in enumerate(m[0]):
        if x != 0:
            stringFuture = str(m[0][x+1:])
            prev = m[0][x-1]
            dub = prev + i

            for l in r:
                if dub == l[0]:
                    mol = (stringPast + l[2] + stringFuture)

                    if mol not in molecules:
                        molecules.append(mol)

            if x != 0:
                stringPast += prev

    return molecules


@time_it
def Part_1(d,m):
    r = Convert_Replacements(d)
    singles = Check_Singles(m,r)
    doubles = Check_Doubles(m,r)
    molecules = singles
    for a in doubles:
        if a not in molecules:
            molecules.append(a)

    for a in molecules:
        print(a)

    print(len(molecules))


Part_1(data,m1)