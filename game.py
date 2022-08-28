import random

class Persona:
    hero_inventory = ["gun", "red_potion"]
    enemy_inventory = []

    def __init__(self, name, health=100):
        self.name=name
        self.health=health

    def attack(self):
        self.health -= random.randrange(10,20)
        if self.health <= 0:
            print(str(self.health) + " " + self.name + " has fallen ")
        else:
            print(str(self.health) + " " + self.name + " is brushed! ")

    def heal(self):
        for i in self.hero_inventory:
            if i == "red_potion":
                self.health += random.randrange(10,20)
                print(str(self.health) + " " + self.name + " was heald!! ")
                self.hero_inventory.remove(i)

    def enemy_drop(self):
        if self.enemy_inventory == True:
            print(self.name + " has picked up a item")
            self.hero_inventory.append(self.enemy_inventory[0])
            self.enemy_inventory.remove()
        else:
            print(self.name + " out of breath, but a live you press forward")

    def hero_drop(self):
        if self.hero_inventory == True:
            print(self.name + " has taken a item")
            self.enemy_inventory.append(self.hero_inventory[0])
            self.hero_inventory.remove()
        else:
            print(self.name + " has insinerated your courps")

    def p_inventory(self):
        i = self.hero_inventory
        print(i)

    def e_inventory(self):
        i = self.enemy_inventory
        print(i)

class Enemy(Persona):
    def __init__(self):
        super().__init__("Combatend1")

class Hero(Persona):
    def __init__(self):
        super().__init__("Player")

e = Enemy()
h = Hero()

while h.health > 0:

    turn = input("Your turn: ")

    if turn == "w":
        e.attack()
        h.attack()

    elif turn == "d":
        h.heal()

    elif turn == "a":
        h.p_inventory()
        e.e_inventory()

    elif turn == "x":
        break

    if h.health <= 0:
        e.hero_drop()
        print("GAME OVER")

    elif e.health <= 0:
        h.enemy_drop()

