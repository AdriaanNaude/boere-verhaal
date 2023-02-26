import random

class player_Persona:
    player_inventory = ["gun", "meds" ]
    base_attack_player = random.randrange(10,20)

    def __init__(self, name, health=100):
        self.name=name
        self.health=health

    def reset(self):
        self.health = 100

# player actions
    def player_attack(self):
        self.health -= self.base_attack_player
        if self.health <= 0:
            print(str(self.health) + " " + self.name + " has fallen ")
        else:
            print(str(self.health) + " " + self.name + " is brushed! ")


# inventory actions

    def heal(self):
        for i in self.player_inventory:
            if i == "meds":
                if self.health != 100:
                    self.health += random.randrange(10,20)
                    print(str(self.health) + " " + self.name + " was heald!! ")
                    self.player_inventory.remove(i)
                else:
                    print("Health is Full")

    def itemAttack(self):
        for i in self.player_inventory:
            if i == "gun":
                totalDamage = self.base_attack_player + 10
                self.health -= totalDamage
                print(str(self.health) + " " + self.name + " was attacked by player with gun! ")

            elif i == "knife":
                totalDamage = self.base_attack_player + 5
                self.health -= totalDamage
                print(str(self.health) + " " + self.name + " was attacked by palyer with knife! ")

# drop systems
    def player_drop(self):
        count = len(self.player_inventory)
        if count > 0:
            print(self.name + " has taken a item")
            self.enemy_inventory.append(self.player_inventory[0])
            self.player_inventory.remove(self.player_inventory[0])
        else:
            print(self.name + " has insinerated your courps")

# inventory interaction systems
    def p_inventory(self):
        i = self.player_inventory
        print(i)


