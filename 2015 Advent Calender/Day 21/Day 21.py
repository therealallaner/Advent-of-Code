
Day_21 = "RPG Simulator 20XX"

player_turn = True

class Character:
    def damage(self, attackdmg):
        attackdmg = attackdmg - self.armor
        if attackdmg <= 0:
            attackdmg = 1
        self.HP -= attackdmg


class Boss(Character):
    def __init__(self, HP, dmg, armor):
        self.HP = HP
        self.dmg = dmg
        self.armor = armor


class Player(Character):
    def __init__(self):
        self.gold_spent = 0
        self.HP = 100
        self.armor = 4


class Weapon:
    def __init__(self, cost, dmg):
        self.cost = cost
        self.dmg = dmg

    def attack(self, target):
        target.damage(self.dmg)
        

class Armor:
    def __init__(self, cost, armor):
        self.cost = cost
        self.armor = armor


class Ring:
    def __init__(self, cost, dmg, armor):
        self.cost = cost
        self.dmg = dmg
        self.armor = armor


p = Player()
b = Boss(100, 12, 1)

dagger = Weapon(8, 4)
shortsword = Weapon(10, 5)
warhammer = Weapon(25, 6)
longsword = Weapon(40, 7)
greataxe = Weapon(74, 8)


while p.HP >= 0 and b.HP >= 0:
    if player_turn:
        warhammer.attack(b)
        player_turn = False
    else:
        p.damage(b.dmg)
        player_turn = True

print("Player HP =", p.HP)
print("Boss HP =", b.HP)