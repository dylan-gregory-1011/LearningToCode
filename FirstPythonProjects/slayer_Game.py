"""
A next forray into object oriented programming.  If role based fighting games with hilarious characters is your thing
then this is the game for you.  This is based on the same type of game as the pokemon type battle game and will
inspire as much fun as comments that the classes and methods should be in different files (I know. cut 2016
me some slack...)
"""

import random
import time

fighters_Names = ["Billy Bob Thorton", "Syndrome", "Mr. T", "Kevin from Accounting", "Gandalf", "Voldemort", "Bernie Bro"]
index = [1,2,3,4,5,6,7]
fighters_Moderate = ['Baseball Bat Bad News Bears', 'Headbutt', "Punch", "Stapler Assualt", 'Staff Wack', 'Snake Attack', 'Trolling a comment section']
fighters_High = ['Slingblading', 'Hairspray Flamethrower', 'Gold Medallion Slam', "Printer Toss", "Spell Curse", 'Avada Kedavra', 'Uninformed Thoughts']
fighters_Heal = ['Solitary Confinement', "Gel Reapplication", 'Healing', "Poop Break", 'Visit the Shire', 'Gets a Nose Job', 'None']

class fighters:

    def __init__(self,Name, Moderate, High, Heal):
        self.Moderate = Moderate
        self.High = High
        self.Heal = Heal
        self.Name = Name

    def fighter_Name(self):
        return self.Name

    def ModerateAttack(self):
        return self.Moderate

    def HighAttack(self):
        return self.High

    def Heal(self):
        return self.Heal


i = 0
while i<len(index):
    index[i] = fighters(fighters_Names[i], fighters_Moderate[i], fighters_High[i], fighters_Heal[i])
    i+=1


print "The fighters available are: "
for names in fighters_Names:
    print names

fighter = raw_input("Who do you want to fight as? ")

enemy_fighter = raw_input("Who do you want to fight against? ")

if fighter in fighters_Names:
    user_fight = fighters_Names.index(fighter)

if enemy_fighter in fighters_Names:
    comp_fight = fighters_Names.index(enemy_fighter)

def fight_Club(index_user, index_comp):

    print "Welcome to Fight Club %s.\nYou better be ready to fight %s" %(fighters_Names[index_user], fighters_Names[index_comp])
    time.sleep(2)
    initial_start = int(raw_input("What number am I thinking between 1 and 2? "))

    inital_Attack = random.randint(1,2)
    time.sleep(1)
    if (initial_start==inital_Attack):
        print "Congrats, you get to go first!"
        person = 'user'
    else:
        print "Darn, you lost. Looks like %s goes first!\n" % fighters_Names[index_comp]
        person = 'comp'
    health_user = 100
    health_comp = 100
    time.sleep(1)
    while (health_comp>0) or (health_user>0):
        health_comp, health_user = Attack(person, health_user, health_comp, index_user, index_comp)
        time.sleep(1)
        if (health_user == 0):
            print "you got your ass kicked. Better luck next time"
            break
        if(health_comp==0):
            print "You won! Congrats!!!"
            break
        if (person == 'comp'):
            person = 'user'
            continue
        if (person == 'user'):
            person = 'comp'
            continue


def Moderate_Attack_Damage():
    damage = random.randint(18,25)
    return damage

def High_Attack_Damage():
    damage = random.randint(10,35)
    return damage

def Heal_Damage():
    damage = random.randint(15,20)
    return damage

def Attack(Person, health_user, health_comp, index_user, index_comp):
    if (Person == 'user'):
        print "You have %i hp left and %s has %i hp left." % (health_user, fighters_Names[index_comp], health_comp)
        print "Your available moves are:\n1.%s with 10-35 damage\n2.%s with 18-25 damage\n3.%s with 15-20 healing"%(index[index_user].HighAttack(),index[index_user].ModerateAttack(),index[index_user].Heal)
        move = raw_input("Select 1,2 or 3: ")
        time.sleep(2)
        if(move == '1'):
            damage_done = High_Attack_Damage()
            health_comp -= damage_done
            if (health_comp<0):
                health_comp = 0
            print "\nYour move %s did %i damage to %s.\nHe has %i hp left\n" % (index[index_user].HighAttack(), damage_done, fighters_Names[index_comp],health_comp)
            return health_comp, health_user
        elif(move == '2'):
            damage_done = Moderate_Attack_Damage()
            health_comp-=damage_done
            if (health_comp<0):
                health_comp = 0
            print "\nYour move %s did %i damage to %s.\nHe has %i hp left\n" % (index[index_user].ModerateAttack(), damage_done, fighters_Names[index_comp],health_comp)
            return health_comp, health_user
        elif(move == '3'):
            damage_done = Heal_Damage()
            health_user+= damage_done
            if(health_user>100):
                health_user = 100
            print '\nYour healing move %s healed you back to %i hp\n' % (index[index_user].Heal, health_user)
            return health_comp, health_user

    if (Person == 'comp'):
        print "You have %i hp left and %s has %i hp left." % (health_user, fighters_Names[index_comp], health_comp)
        #print "His available moves are:\n1.%s with 10-35 damage\n2.%s with 18-25 damage\n3.%s with 15-20 healing"%(index[index_comp].HighAttack(),index[index_comp].ModerateAttack(),index[index_comp].Heal)
        if (health_comp<35):
            move = random.randint(2,3)
        else:
            move = random.randint(1,3)
        time.sleep(2)
        if(move == 1):
            damage_done = High_Attack_Damage()
            health_user -= damage_done
            if (health_user<0):
                health_user = 0
            print "\n%s\'s move %s did %i damage to %s.\nYou have %i hp left\n" % (fighters_Names[index_comp], index[index_comp].HighAttack(), damage_done, fighters_Names[index_user],health_user)
            return health_comp, health_user
        elif(move == 2):
            damage_done = Moderate_Attack_Damage()
            health_user-=damage_done
            if (health_user<0):
                health_user = 0
            print "\n%s\'s move %s did %i damage to %s.\nHe has %i hp left\n" % (fighters_Names[index_comp],index[index_comp].ModerateAttack(), damage_done, fighters_Names[index_user],health_user)
            return health_comp, health_user
        elif(move == 3):
            damage_done = Heal_Damage()
            health_comp+= damage_done
            if(health_comp>100):
                health_comp = 100
            print '\n%s\'s healing move %s healed him back to %i hp\n' % (fighters_Names[index_comp],index[index_comp].Heal(), health_comp)
            return health_comp, health_user

fight_Club(user_fight, comp_fight)
