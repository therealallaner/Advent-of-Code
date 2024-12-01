from utils.mymethods import Data_to_List
import random
from utils.decorators import time_it

Day_21 = "RPG Simulator 20XX"


#instead of buyind loadouts and seeing if they work starting from an infinit amount of money, i am going to restrict the amount of 
# money available to be used in the store and try all possible loadouts with that number until i find something cheaper.


data = Data_to_List(2015,21,'store')

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


def Buy_Weapon(Weapons,weaponsList):
    weapon = random.choice(weaponsList)
    return Weapons[weapon]

def Buy_Armor(Armor,armorList):
    
    if random.random() >= .1:
        a = random.choice(armorList)
        return Armor[a]
            
    else:
        return 0,0,0
        

def Buy_Rings(Rings,ringsList):

    rings = []
    x = random.randint(0,2)
    while len(rings) < x:
        r = random.choice(ringsList)
        if r not in rings:
            rings.append(r)

    cost = 0
    dmg = 0
    ac = 0

    if rings:
        for r in rings:
            cost += Rings[r][0]
            dmg += Rings[r][1]
            ac += Rings[r][2]

    return cost,dmg,ac



def Buy_Loadout(w,wl,a,al,r,rl):

    weapon = Buy_Weapon(w,wl)

    armor = Buy_Armor(a,al)

    ring = Buy_Rings(r,rl)

    cost = weapon[0] + armor[0] + ring[0]
    dmg = weapon[1] + ring[1]
    ac = armor[2] + ring[2]

    return cost,dmg,ac


def Boss_Fight(Weapons,weaponsList,Armor,armorList,Rings,ringsList):

    l = Buy_Loadout(Weapons,weaponsList,Armor,armorList,Rings,ringsList)
    cost = l[0]
    dmg = l[1]
    ac = l[2]

    playerHP = 100
    playerDmg = dmg
    playerAC = ac

    bossHP = 103
    bossDmg = 9
    bossAC = 2


    playerAttack = playerDmg - bossAC
    if playerAttack <= 0:
        playerAttack = 1

    bossAttack = bossDmg - playerAC
    if bossAttack <= 0:
        bossAttack =1

    fightLog = []
    fighting = True
    playerTurn = True
    while fighting:
        if playerTurn:
            bossHP -= playerAttack
            playerTurn = False
            fightLog.append(f'Boss took {playerAttack} and is now at {bossHP} HP.')
            if bossHP <= 0:
                fighting = False
                #print('')
                #print(f'Gold used {cost}.')
                #print('')

        else:
            playerHP -= bossAttack
            playerTurn = True
            fightLog.append(f'Player took {bossAttack} and is now at {playerHP} HP.')
            if playerHP <= 0:
                fighting = False
                #print('')
                #print(f'Gold used {cost} and you didnt even kill the boss...')
                #print('')
                return cost


highestCost = 100
for x in range(10000):
    c = Boss_Fight(Weapons,weaponsList,Armor,armorList,Rings,ringsList)
    if c:
        if c > highestCost:
            highestCost = c

print(highestCost)