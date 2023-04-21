import random
from player import *
from enemy import *

class Enemy(ePersona):
    def __init__(self):
        super().__init__("Combatend1")

class player(player_Persona):
    def __init__(self):
        super().__init__("Player")

e = Enemy()
p = player()

def item_use(user_input):
    if user_input == "i":
      x = input("Item?: ")
    if x == "1":
        p.heal()
    elif x == "2":
        e.itemAttack()    

def quit_game(user_input):
    if user_input == "x":
        print("Do you want to Quit? [Y/N]")
        opt = input(">> ")

        if opt == "y" or turn == "Y":
            pass
        elif opt == "n" or turn == "N":
            print("I will stay")


# game loop

while p.health > 0:

    turn = input("Your turn: ")

    if turn == "w":
        e.enemy_attack()
        p.player_attack()

    elif turn == "i":
        p.p_inventory()
        item_use(turn)

    elif turn == "x":
        #quit_game(turn)
        print("Do you want to Quit? [Y/N]")
        opt = input(": ")
        if opt == "y" or opt == "Y":
            break
        elif opt == "n" or turn == "N":
            print("I will stay")
        else:
            "Not a option"
        
    if p.health is int and p.health <= 0:
        e.player_drop()
        print("GAME OVER")

    elif e.health <= 0:
        p.enemy_drop()
        e.reset()
