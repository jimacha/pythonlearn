import random
import math

class Warrior:

    def __init__(self, name="warrior", health=0, attmax=0, blockmax=0):
        self.name = name
        self.health = health
        self.attmax = attmax
        self.blockmax = blockmax

    def attack(self):
        attant = self.attmax*(random.random() + .5)
        return attant
    def block(self):
        blcant = self.blockmax*(random.random() + .5)
        return blcant
    
class Battle:
    def lfight(self, warrior1, warrior2):

        while True: # we use this if we want it to loop but we do not know for how long
            if self.lresult(warrior1, warrior2) == "game over":
                print("game over")
                break
            if self.lresult(warrior2, warrior1) == "game over":
                print("game over")
                break
    @staticmethod #the method doesn't have to refer to itself,all the information that it needs is passed from the attribute
    def lresult(warriorA, warriorB):
        warriorAattant=warriorA.attack()
        warriorBblockant=warriorB.block()
        warriorBdamage = math.ceil(warriorAattant-warriorBblockant)

        warriorB.health = warriorB.health - warriorBdamage

        print("{} is attacks {} and deals {} damages".format(warriorA.name, warriorB.name, warriorBdamage))
        print("{} is down with a health of{}".format(warriorB.name, warriorB.health))
        
        if warriorB.health <= 0:
            return "gameover"
        else:
            return "continue"
        
    def main():
        maximus = warrior("maximus", 50, 20, 10)
        gules = warrior("gules", 50, 20, 10)

        battle = Battle()

        battle.lfight(maximus,gules)
    main()