from utils.mymethods import Data_to_List
import random
from utils.decorators import time_it

Day_21 = "RPG Simulator 20XX"


Weapons = {
    'dagger': [8,4,0],
    'shortsword': [10,5,0],
    'warhammer': [25,6,0],
    'longsword': [40,7,0],
    'greataxe': [74,8,0]
}
weaponsList = ['dagger','shortsword','warhammer','longsword','greataxe']


Armor = {
    'leather': [13,0,1],
    'chainmail': [31,0,2],
    'splintmail': [53,0,3],
    'bandedmail': [75,0,4],
    'platemail': [102,0,5]
}
armorList = ['leather','chainmail','splintmail','bandedmail','platemail']


Rings = {
    'sapphire': [25,1,0],
    'ruby': [50,2,0],
    'diamond': [100,3,0],
    'iron': [20,0,1],
    'gold': [40,0,2],
    'netherite': [80,0,3]
}
ringsList = ['sapphire','ruby','diamond','iron','gold','netherite']


Boss = {
    'HP': 103,
    'Damage': 9,
    'AC': 2
}

Player = {
    'HP': 100,
    'Damage': 0,
    'AC': 0
}


def Buy_Weapon(Weapons,weaponsList):
    w = random.choice(weaponsList)
    weaponCost = Weapons[w][0]
    playerDamage = Weapons[w][1]

    return weaponCost, playerDamage


def Buy_Armor(Armor,armorList):
    if random.random() >= .1:
        a = random.choice(armorList)
        armorCost = Armor[a][0]
        playerAC = Armor[a][2]
    else:
        armorCost = 0
        playerAC = 0

    return armorCost, playerAC
    

def Buy_Rings(Rings,ringsList):
    rando = random.randint(0,2)
    rings = []

    while len(rings) < rando:
        r = random.choice(ringsList)
        if r not in rings:
            rings.append(r)

    ringCost = 0
    playerDamage = 0
    playerAC = 0

    if rings:
        for r in rings:
            ringCost += Rings[r][0]
            playerDamage += Rings[r][1]
            playerAC += Rings[r][2]

    return ringCost, playerDamage, playerAC


def Get_Loadout(Weapons,weaponsList,Armor,armorList,Rings,ringsList):

    w = Buy_Weapon(Weapons,weaponsList)
    a = Buy_Armor(Armor,armorList)
    r = Buy_Rings(Rings,ringsList)

    cost = (w[0] + a[0] + r[0])
    playerDamage = (w[1] + r[1])
    playerAC = (a[1] + r[2])


    return cost, playerDamage, playerAC


def Boss_Fight(Weapons,weaponsList,Armor,armorList,Rings,ringsList,Boss,Player):
    fightLog = []
    loadout = Get_Loadout(Weapons,weaponsList,Armor,armorList,Rings,ringsList)

    goldSpent = loadout[0]
    Player['Damage'] = loadout[1]
    Player['AC'] = loadout[2]


    if (Player['Damage'] - Boss['AC']) <= 1:
        playerDMG = 1
    else:
        playerDMG = Player['Damage'] - Boss['AC']

    if (Boss['Damage'] - Player['AC']) <= 1:
        bossDMG = 1
    else:
        bossDMG = Boss['Damage'] - Player['AC']


    fighting = True
    playerTurn = True
    while fighting:
        if playerTurn:
            Boss['HP'] -= playerDMG
            fightLog.append(f'Boss takes {playerDMG} and is now at {Boss['HP']}')
            playerTurn = False
            
            if Boss['HP'] <= 0:
                fighting = False
                if goldSpent <= 200:
                    for l in fightLog:
                        print(l)
                    print(goldSpent)
                return goldSpent
        else:
            Player['HP'] -= bossDMG
            fightLog.append(f'Player takes {bossDMG} and is now at {Player['HP']}')
            playerTurn = True
            if Player['HP'] <= 0:
                fighting = False

@time_it
def Simulate_Runs(Weapons,weaponsList,Armor,armorList,Rings,ringsList,Boss,Player):
    winningCosts = []
    lowestCost = 200
    for x in range(15000000):
        Boss['HP'] = 103
        c = Boss_Fight(Weapons,weaponsList,Armor,armorList,Rings,ringsList,Boss,Player)
        if c:
            winningCosts.append(c)
            if c < lowestCost:
                lowestCost = c

    print(winningCosts)
    print(lowestCost)


Simulate_Runs(Weapons,weaponsList,Armor,armorList,Rings,ringsList,Boss,Player)

