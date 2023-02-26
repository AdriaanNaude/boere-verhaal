import random

class ePersona:
    enemy_inventory = ["ammo", "knife", "meds"]
    base_attack_enemy = random.randrange(15, 30)

    def __init__(self, name, health=100):
        self.name=name
        self.health=health

    def reset(self):
        self.health = 100

# enemy actions

    def enemy_attack(self):
        self.health -= self.base_attack_enemy
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
    def enemy_drop(self):
        for i in self.enemy_inventory:
            
            print(self.name + " has picked up a item")
            self.player_inventory.append(self.enemy_inventory)
            #self.enemy_inventory.remove()
        else:
            print(self.name + " out of breath, but alive you press forward")

# inventory interaction systems
    def e_inventory(self):
        i = self.enemy_inventory
        print(i)



