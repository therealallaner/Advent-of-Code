from utils.decorators import time_it
from utils.mymethods import Data_to_List
import random


Day_11 = "Radioisotope Thermoelectric Generators"


data = Data_to_List(2016,11,"data")
testActions = ["up","down","pickup"]

class bot:
    def __init__(self,floor,gen,steps):
        self.floor = floor
        self.gen = gen
        self.steps = self.MutateSteps(steps)

    def MutateSteps(self,steps):
        x = random.randint(1,100)
        if x <= 10:
            print(25)
            print("")
            return 25
        else:
            print("")
            return 12

p1 = bot(1,1,testActions)

for x in range(100):
    print(x)
    x = bot(1,1,testActions)
