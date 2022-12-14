import random

class Persona:
    player_inventory = ["gun", "red_potion"]
    enemy_inventory = []
    base_attack_player = random.randrange(10,20)
    base_attack_enemy = random.randrange(15, 30)

    def __init__(self, name, health=100):
        self.name=name
        self.health=health

    def reset(self):
        self.health = 100

    # actions
    def enemy_attack(self):
        self.health -= self.base_attack_enemy
        if self.health <= 0:
            print(str(self.health) + " " + self.name + " has fallen ")
        else:
            print(str(self.health) + " " + self.name + " is brushed! ")

    def player_attack(self):
        self.health -= self.base_attack_player
        if self.health <= 0:
            print(str(self.health) + " " + self.name + " has fallen ")
        else:
            print(str(self.health) + " " + self.name + " is brushed! ")
             
    def heal(self):
        for i in self.player_inventory:
            if i == "red_potion":
                self.health += random.randrange(10,20)
                print(str(self.health) + " " + self.name + " was heald!! ")
                self.player_inventory.remove(i)

    def enemy_drop(self):
        if self.enemy_inventory == True:
            print(self.name + " has picked up a item")
            self.player_inventory.append(self.enemy_inventory[0])
            self.enemy_inventory.remove()
        else:
            print(self.name + " out of breath, but a live you press forward")

    def player_drop(self):
        count = len(self.player_inventory)
        if count > 0:
            print(self.name + " has taken a item")
            self.enemy_inventory.append(self.player_inventory[0])
            self.player_inventory.remove(self.player_inventory[0])
        else:
            print(self.name + " has insinerated your courps")

    # game systems
    def p_inventory(self):
        i = self.player_inventory
        print(i)

    def e_inventory(self):
        i = self.enemy_inventory
        print(i)

class Enemy(Persona):
    def __init__(self):
        super().__init__("Combatend1")

class player(Persona):
    def __init__(self):
        super().__init__("Player")

e = Enemy()
p = player()

def item_use(user_input):
    if user_input == "i":
      x = input("Item?: ")
    if x == "1":
        p.heal()
    """
    elif x == "2"
        e.attack()    
    """
while p.health > 0:

    turn = input("Your turn: ")

    if turn == "w":
        e.enemy_attack()
        p.player_attack()

    # inventory system aanwerk
    elif turn == "i":
        p.p_inventory()
        item_use(turn)

    elif turn == "x":
        break

    if p.health <= 0:
        e.player_drop()
        print("GAME OVER")

    elif e.health <= 0:
        p.enemy_drop()
        e.reset()
