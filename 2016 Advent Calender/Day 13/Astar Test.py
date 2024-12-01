from utils.decorators import time_it
from utils.mymethods import Data_to_List
from pdb import set_trace as bp


Day_13 = "A Maze of Twisty Little Cubicles"
puzzleInput = 1364
test = 10
myMaze = 41
data = 1364
yLineRender = ['   0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3 3 3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 5 5 5 5 5 5 5 5 5 5',
         '   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9']
# Find x*x + 3*x + 2*x*y + y + y*y

yLineBot = []


def WallorNah(x,y,s,beenThere):
    b = 0

    q = (x*x) + (3*x) + (2*x*y) + (y) + (y*y)
    q += data

    #print("")
    #print(q)
    #print(str(bin(q).lstrip('0b')))
    w = str(bin(q).lstrip('0b'))
    for i in w:
        #print(i)
        if i == "1":
            b += 1
            #print(b)


    if data == 10:
        if x == 7:
            if y == 4:
                return "O"
    else:
        if x == 31:
            if y == 39:
                return "O"
     
    if (x,y) in beenThere:
        return "X"

    if (b%2) == 0:
        #print(b)
        return "."
    else:
        return "#"
    

@time_it
def GenMaze(d,s,beenThere):
    b = beenThere
    data = d
    for l in range(60):
        xStringBot = ''
        if l > 9:
            xStringRender = f'{l} '
        else:
            xStringRender = f' {l} '

        for i in range(60):
            xStringRender += WallorNah(i,l,s,b)
            xStringBot += WallorNah(i,l,s,b)
            xStringRender += ' '

        yLineRender.append(xStringRender)
        yLineBot.append(xStringBot)


    for l in yLineRender:
        print(l)

    return yLineBot


def GetManhatten(b,t):
    x = b[-1][0]
    y = b[-1][1]
    tx = t[0]
    ty = t[1]
    path = []

    while x != tx:
        x += 1
        path.append((x,y))
    
    while y != ty:
        y += 1
        path.append((x,y))

    return path


def checkManhatten(m,b,p):
    currentPos = b[-1]
    desiredPos = p[0]
    x = desiredPos[0]
    y = desiredPos[1]

    if m[y][x] == ".":
        currentPos == desiredPos
    else:
        



def aStar(m,t,b):
    path = GetManhatten(b,t)
    checkManhatten(m,b,path)
    


def Main():
    beenThere = [(0,0)]
    maze = GenMaze(data,False,beenThere)
    target = (0,0)
    for y, l in enumerate(maze):
        for x, i in enumerate(l):
            if i == "O":
                target = (x,y)

    aStar(maze,target,beenThere)


Main()