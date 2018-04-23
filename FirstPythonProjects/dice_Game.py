"""
To keep in line with the other gambling games, allows the user to play a rousing game of craps.
"""
import random
import time

def craps():
    print "Welcome to Dylan's Casino.  \nWe have one game and one game only.  \nYou feelin lucky????"
    time.sleep(3)
    print
    play = raw_input('We\'re playing craps. Are you Ready?? Y/N??')
    dice_One = 1
    dice_Two = 1
    play_On = 'Y'
    winnings= 0
    while play.upper() != 'N':
        bets = int(raw_input('What is your Pass Line bet?'))
        dice_One = random.randint(1,6)
        dice_Two = random.randint(1,6)
        print 'you rolled a %i and a %i' %(dice_One, dice_Two)
        if (dice_One+dice_Two==2) or (dice_One+dice_Two==3) or (dice_One+dice_Two==12):
            print 'You crapped out... better luck next time.'
            winnings -= bets
        elif (dice_One+dice_Two==7) or (dice_One+dice_Two== 11):
            print 'You got a natural on your come out roll!! Lets play again!'
            winnings += bets
        else:
            point = dice_One+ dice_Two
            play_On = 'Y'
            while play_On == 'Y':
                print "You need a %i to win" %(point)
                rolling = raw_input("Ready to roll again?")
                dice_One = random.randint(1,6)
                dice_Two = random.randint(1,6)
                print 'you rolled a %i and a %i' %(dice_One, dice_Two)
                if (dice_One+dice_Two==7):
                    print "You 7\'ed out.."
                    winnings -= bets
                    break
                if(dice_One+dice_Two==point):
                    print "You won the point!!!"
                    winnings +=bets
                    break
                print "You didnt pass or win..."
        play = raw_input("Do you want to play again??")
    if (winnings == 0):
        print "You didnt win, but you didnt lose!!"
    if (winnings<0):
        print "You owe me %i dollars, give it to me or ill take it..." % (winnings)
    if (winnings>0):
        print "You won %i dollars... You got lucky this time!!!" % (winnings)
craps()
