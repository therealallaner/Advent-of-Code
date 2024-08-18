from utils.decorators import time_it
from utils.mymethods import Data_to_List
from pdb import set_trace as bp


Day_13 = "A Maze of Twisty Little Cubicles"
puzzleInput = 1364
test = 10
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


# Maze Try 1 will always try to move down, then right, then left, then up. Will not go back on the previous move it just did. 
def MazeTry1(maze,botPos,beenThere):

    validSpots = [
        '.',
        'T',
        'O'
    ]

    x = botPos[0]
    y = botPos[1]


    # Down
    if maze[y+1][x] in validSpots:
        down = x,(y+1)
        if down not in beenThere:
            return down
    
    # Right
    if maze[y][x+1] in validSpots:
        right = (x+1),y
        if right not in beenThere:
            return right
    
    # Left
    if maze[y][x-1] in validSpots:
        left = (x-1),y
        if left not in beenThere:
            return left
    
    # Up
    if maze[y-1][x] in validSpots:
        up = x,(y-1)
        if up not in beenThere:
            return up
    
    return "Got Stuck"



# This 'bot' will always keep its 'left hand' on the wall.
# This actually works but I need the most efficient path.

def HandonWall(maze,botPos,beenThere):
    validSpots = [
        '.',
        'T',
        'O'
    ]
    x = botPos[0]
    y = botPos[1]

    botFacing = ''
    previousPos = beenThere[-1]
    up = x,y-1
    left = x-1,y
    down = x,y+1
    right = x+1,y


    # This checks and sets the direction the bot should be facing
    if previousPos == (0,0):
        botFacing = 'right'

    else:
        if previousPos == down:
            botFacing = 'up'

        elif previousPos == right:
            botFacing = 'left'

        elif previousPos == up:
            botFacing = 'down'

        elif previousPos == left:
            botFacing = 'right'

    # This checks wether or not the bot can move forward depending on where it is facing
    if botFacing == 'down':
        #look left to see if a wall is next to it
        if maze[y][x+1] == "#":
            #space in front clear?
            if maze[y+1][x] in validSpots:
                # move forward
                return down
            #Space in front is not clear so check to its right
            else:
                # checks to its right
                if maze[y][x-1] in validSpots:
                    return left
                else:
                    # dead end turn around still following the wall
                    return up
        else:
            #does it need to turn to keep following the wall?
            return right
        

    elif botFacing == 'right':
        if maze[y-1][x] == "#":
            if maze[y][x+1] in validSpots:
                return right
            else:
                if maze[y+1][x] in validSpots:
                    return down
                else:
                    return left
        else:
            return up

    elif botFacing == 'up':
        if maze[y][x-1] == "#":
            if maze[y-1][x] in validSpots:
                return up
            else:
                if maze[y][x+1] in validSpots:
                    return right
                else:
                    return down
        else:
            return left
        
    elif botFacing == 'left':
        if maze[y+1][x] == "#":
            if maze[y][x-1] in validSpots:
                return left
            else:
                if maze[y-1][x] in validSpots:
                    return up
                else:
                    return right
        else:
            return down
        
    else:
        return "Stop"
        

# 1 check all available spots
# 2 if more than current number of bots, make a new bot
# 3 if a bot runs into a path of another bot, it is deleted
        # might now actually do this cause it might not matter
# 4 keep searching till shortest path to target is found

def BreadthFirstSearch(maze,t,p,steps):


    validSpots = [
        '.',
        'T',
        'O',
        'W'
    ]

    newBots = []
    currentPos = p
    x = currentPos[0]
    y = currentPos[1]

    target = t

    up = x,y-1
    left = x-1,y
    down = x,y+1
    right = x+1,y


    # This puts borders around the maze
    if y != 0:
        mazeUp = maze[y-1][x]
    else:
        mazeUp = "#"

    if x != 0:
        mazeLeft = maze[y][x-1]
    else: 
        mazeLeft = "#"

    if y != 59:
        mazeDown = maze[y+1][x]
    else: 
        mazeDown = "#"

    if x != 59:
        mazeRight = maze[y][x+1]
    else:
        mazeRight = "#"



    # This is the Target Position
    if maze[y][x] == "O":
        if len(steps) < 90:
            print(len(steps)-1)
        return True
    

#    if maze[y][x] == "W":
#       print(steps)
#        print(len(steps)-1)
#        return True


    # Checks for Valid Moves
    if mazeUp in validSpots:
        if up not in steps:
            stepsUp = []
            for s in steps:
                stepsUp.append(s)
            stepsUp.append(up)
            newBots.append(up)


    if mazeLeft in validSpots:
        if left not in steps:
            stepsLeft = []
            for s in steps:
                stepsLeft.append(s)
            stepsLeft.append(left)
            newBots.append(left)
    

    if mazeDown in validSpots:
        if down not in steps:
            stepsDown = []
            for s in steps:
                stepsDown.append(s)
            stepsDown.append(down)
            newBots.append(down)
            
    if mazeRight in validSpots:
        if right not in steps:
            stepsRight = []
            for s in steps:
                stepsRight.append(s)
            stepsRight.append(right)
            newBots.append(right)




    for l in newBots:
        if l == up:
            BreadthFirstSearch(maze,t,l,stepsUp)
        if l == left:
            BreadthFirstSearch(maze,t,l,stepsLeft)
        if l == down:
            BreadthFirstSearch(maze,t,l,stepsDown)
        if l == right:
            BreadthFirstSearch(maze,t,l,stepsRight)
        

@time_it
def Part1():
    active = True
    beenThere = [(0,0)]
    maze = GenMaze(data,False,beenThere)
    botPos = (1,1)
    target = 7,4
    #while active:
    #    #step = MazeTry1(maze,botPos,beenThere)
    #    step = HandonWall(maze,botPos,beenThere)
    #    if str(step[0]).isnumeric():
    #        beenThere.append(botPos)
    #        botPos = step
    #        if botPos == target:
    #            beenThere.append(botPos)
    #            active = False
    #    else:
    #        active = False
            

    #for l in beenThere:
    #    print(l)
    #print(len(beenThere)-2)

    steps = [(1,1)]
    BreadthFirstSearch(maze,target,botPos,steps)

#    for l in beenThere:
#        print(l)



def BreadthFirstSearch2(maze,p,steps,beenThere):


    validSpots = [
        '.',
        'T',
        'O',
        'W'
    ]

    newBots = []
    currentPos = p
    x = currentPos[0]
    y = currentPos[1]


    up = x,y-1
    left = x-1,y
    down = x,y+1
    right = x+1,y


    # This puts borders around the maze
    if y != 0:
        mazeUp = maze[y-1][x]
    else:
        mazeUp = "#"

    if x != 0:
        mazeLeft = maze[y][x-1]
    else: 
        mazeLeft = "#"

    if y != 59:
        mazeDown = maze[y+1][x]
    else: 
        mazeDown = "#"

    if x != 59:
        mazeRight = maze[y][x+1]
    else:
        mazeRight = "#"



    if currentPos not in beenThere:
        beenThere.append(currentPos)


    if len(steps) <= 50:

        # Checks for Valid Moves
        if mazeUp in validSpots:
            if up not in steps:
                stepsUp = []
                for s in steps:
                    stepsUp.append(s)
                stepsUp.append(up)
                newBots.append(up)


        if mazeLeft in validSpots:
            if left not in steps:
                stepsLeft = []
                for s in steps:
                    stepsLeft.append(s)
                stepsLeft.append(left)
                newBots.append(left)
    

        if mazeDown in validSpots:
            if down not in steps:
                stepsDown = []
                for s in steps:
                    stepsDown.append(s)
                stepsDown.append(down)
                newBots.append(down)
                
        if mazeRight in validSpots:
            if right not in steps:
                stepsRight = []
                for s in steps:
                    stepsRight.append(s)
                stepsRight.append(right)
                newBots.append(right)

    else:
        print("")
        print("")
        #GenMaze(data,True,beenThere)
        print(len(beenThere))
        return


    for l in newBots:
        if l == up:
            BreadthFirstSearch2(maze,l,stepsUp,beenThere)
        if l == left:
            BreadthFirstSearch2(maze,l,stepsLeft,beenThere)
        if l == down:
            BreadthFirstSearch2(maze,l,stepsDown,beenThere)
        if l == right:
            BreadthFirstSearch2(maze,l,stepsRight,beenThere)


@ time_it
def Part2():
    beenThere = []
    maze = GenMaze(data,False,beenThere)
    botPos = (1,1)
    steps = [(1,1)]

    BreadthFirstSearch2(maze,botPos,steps,beenThere)



#Part1()
Part2()
#GenMaze(data)