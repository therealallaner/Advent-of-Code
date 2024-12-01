from utils.mymethods import Data_to_List
import random
from utils.decorators import time_it

Day_21 = "RPG Simulator 20XX"



#   Dagger        8     4       0 i dont think this is possible to use
#   Shortsword   10     5       0
#   Warhammer    25     6       0
#   Longsword    40     7       0
#   Greataxe     74     8       0

#   Leather      13     0       1
#   Chainmail    31     0       2
#   Splintmail   53     0       3
#   Bandedmail   75     0       4
#   Platemail   102     0       5 i dont think this is possible to use

#   Sapphire     25     1       0
#   Ruby         50     2       0
#   Diamond     100     3       0 i dont think this is possible to use
#   Iron         20     0       1
#   Gold         40     0       2
#   Netherite    80     0       3


weapon = 'longsword'
armor = 'leather'
right = 'gold'
left = 'ruby'

playerHP = 100
playerDmg = 0
playerAC = 0
goldCost = 0

bossHP = 103
bossDmg = 9
bossAC = 2


data = Data_to_List(2015,21,'store')

for l in data:
    l = l.split()
    cost = int(l[1])
    damage = int(l[2])
    AC = int(l[3])

    if weapon in l:
        goldCost += cost
        playerDmg += damage
    
    if armor in l:
        goldCost += cost
        playerAC += AC
    
    if right in l:
        goldCost += cost
        playerDmg += damage
        playerAC += AC

    if left in l:
        goldCost += cost
        playerDmg += damage
        playerAC += AC


fightLog = []
fighting = True
playerTurn = True
while fighting:
    
    if playerTurn:
        damage = playerDmg-bossAC
        if damage <= 0:
            damage = 1
        bossHP -= (damage)
        fightLog.append(f'The boss took {damage} damage, dropping him from {bossHP+damage} to {bossHP}')
        playerTurn = False
        if bossHP <= 0:
            fighting = False
            for l in fightLog:
                print(l)
            print('')
            print(f'You spent {goldCost} gold on this loadout.')
            print('')

    else:
        damage = bossDmg-playerAC
        if damage <= 0:
            damage = 1
        playerHP -= (damage)
        fightLog.append(f'You took {damage} damage, dropping him from {playerHP+damage} to {playerHP}')
        playerTurn = True
        if playerHP <= 0:
            fighting = False
            for l in fightLog:
                print(l)
            print('')
            print(f'You spent {goldCost} gold on this loadout.')
            print('')
            print('You have failed to kill the boss...')
            print('')

