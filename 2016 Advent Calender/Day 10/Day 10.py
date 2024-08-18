from utils.decorators import time_it
from utils.mymethods import Data_to_List


Day_10 = "Balance Bots"


data = Data_to_List(2016,10,"data")
test = Data_to_List(2016,10,"test")
instructionsCompleted = False
botList = []
outList = []

testlist = [12,355,2125,["test","three"],649654]

### bot 0 gives low to output 2 and high to output 0
### value 2 goes to bot 2

for x in range(220):
    botList.append([])
    outList.append([])


def CompValues(b):
    low = min(b)
    high = max(b)

    return low,high

while len(data) > 0:
    for l in data:
        line = l
        l = l.split()


        if "gives" in l:
            bot = int(l[1])
            if len(botList[bot]) == 2:
                low = CompValues(botList[bot])[0]
                high = CompValues(botList[bot])[1]
                out1 = int(l[6])
                out2 = int(l[11])
                botList[bot] = []

                if low == 17:
                    if high == 61:
                        print("")
                        print(f"Bot {bot} is responsible for comparing the numbers 17 and 61.")
                        print("")


                if l[5] == "bot":
                    botList[out1].append(low)
                else:
                    outList[out1].append(low)

                if l[10] == "bot":
                    botList[out2].append(high)
                else:
                    outList[out2].append(high)
                
                data.remove(line)

        elif "value" in l:
            value = int(l[1])
            bot = int(l[-1])

            botList[bot].append(value)
            data.remove(line)



#### Part 2

print(outList[0][0]*outList[1][0]*outList[2][0])