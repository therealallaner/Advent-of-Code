from utils.decorators import time_it

Day_25 = "Let It Snow"

desiredRow = 3010
desiredColumn =3019

desiredNumMightBe = 4531564

@time_it
def Find_Code(gridNumber):

    firstCode = 20151125
    multiplyValue = 252533
    divideValue = 33554393
    currentCode = firstCode

    for i in range(gridNumber-1):
        currentCode = currentCode * multiplyValue
        currentCode = currentCode % divideValue
    
    return currentCode

@time_it
def Find_Code_Number(r,c):
    rowList = []
    gridNumber = 1
    row = 1
    column = 1
    

    while row < r or column < c:


        gridNumber += 1

        if row not in rowList:
            rowList.append(row)

        if row == 1:
            row = rowList[-1] + 1
            column = 1

        else:
            row -= 1
            column += 1

        if row > rowList[-1]:
            print(row)




    print(f"The desired number should be {gridNumber} at coords {row},{column}")
    return gridNumber





gridNumber = Find_Code_Number(desiredRow,desiredColumn)
Part_1 = Find_Code(gridNumber)
print(f"Part one answer should be {Part_1}")

    