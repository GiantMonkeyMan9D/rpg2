#!/usr/bin/env python


class Wolf:
	def __init__(self):
		self.hp = 25
		self.dmg = 5
                self.df = 0

	def hit(self,dmg):
		self.hp = self.HP - dmg

        def fight(self,attacker):
            print("A WOLF ATTACKS YOU! WHAT DO YOU DO?(ABCD)")
            print("WOLF STATS")
            print("HP="+str(self.hp))
            print("DEF="+str(self.df))
            print("_____________________________________________________________")

            self.attack(attacker)

        def attack(self,attacker):
            while self.hp > 0:
                inputLetter=raw_input("|USE YOUR SWORD|USE MAGIC|PREPARE TO DODGE|PREPARE TO BLOCK|")
                if inputLetter=='a' and attacker.weapon==True:
                        self.hp=self.hp-attacker.dmg
                        print ("YOU DEAL "+str(attacker.dmg)+" DAMAGE")
                        if self.hp <= 0:
                                print("THE WOLF DIED")
                                return
                        print ("WOLF DEALS 5 DAMAGE")
                        attacker.hp=attacker.hp - 5
                elif inputLetter=='a' and attacker.weapon!='true':
                        print("YOU HAVE NO WEAPON")
                elif inputLetter=='b' and attacker.mg>=5:
                        self.hp=self.hp - attacker.mg
                        print("YOU DEAL "+str(attacker.mg)+" DAMAGE")
                              
                print("_____________________________________________________________")
                if self.hp > 0:
                    print("WOLF DOES 5 DAMAGE")
                    attacker.hp = attacker.hp - 5
                    print("_____________________________________________________________")
            
            print("THE WOLF DIED")
            attacker.gainXP(10)

class Bear:
    def __init__(self):
            self.hp = 75
            self.dmg = 15


class Player:
	def __init__(self):
		self.class1 = 'BaseClass'
		self.dmg = 5
		self.mg = 5
		self.dg = 10
		self.hp = 15
		self.weapon = False
                self.xp = 0

                self.changeClass()

	def changeClass(self):
            cClass = 'Error'
	    while(cClass == 'Error'):
	    	cClass = raw_input("DO YOU PREFER (a)MAGIC OR (b)FIGHTING")
	    	if cClass == 'a':
	    		cClass = "Mage"
	    		self.mg = 20
	    	elif cClass == 'b':
	    		cClass = "Fighter"
	    		self.dmg = 10
	    		self.hp = 20
	    		self.weapon = True
	    	else:
	    		cClass = 'Error'
	    		print("Error!  Please choose 'a' or 'b'")
	    self.class1 = cClass

        def gainXP(self,addNumber):
            self.xp = self.xp + addNumber
            print("YOU GAINED "+str(addNumber)+" XP!")
            if self.xp == 10:
                print("IT WORKED")

        
	

def main():
	intro()
        player = Player()
        wolf1 = Wolf()
        wolf1.fight(player)
        direct = direction(player)


def intro():
	print("WELCOME TO RPG1!")

	print("____________________________________________________")
	print("YOU ARE LOST IN A FOREST")
	




def direction(player):
	choose=raw_input("DO YOU GO (a)LEFT OR (b)RIGHT ")
	if choose=='a':
            wolf = Wolf()
	    wolf.fight(player)
            return 'a'
	elif choose=='b':
		print("YOU STEP IN A BOOBY TRAP AND COME FLYING UP TRAPPED IN A NET")
                return 'b'
	else:
		print("choose a or b")
                return 'Error'

if __name__ == "__main__":
	main()
