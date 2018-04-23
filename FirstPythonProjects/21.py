"""
For an inspiring game of 21 (Blackjack), look no further.
"""

import random
import time


def game_21():
    game_round = 1
    score = 100
    print "I hope you are pumped to play 21\nThere will be five rounds and the highest score wins\n"
    print "The difference between your number and 21\nwill be subtracted from your score after every round\n"
    time.sleep(2)
    while game_round<=5:
        print "Welcome to round %i" %(game_round)
        print "You have a score of %i" %(score)
        time.sleep(1)
        round_score = draw_cards(score)
        score_dif = 21- round_score
        if (score_dif<0):
            score_dif = round_score
        score-=score_dif
        game_round+=1

    print "Your final score was %i" %(score)
    print "thanks for playing"
#print "you drew a %s of %s" % (deck.values()[0][1], deck.keys()[0])

def draw_cards(score):
    hearts = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    diamonds = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    clubs =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    spades = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = {'hearts': hearts, 'diamonds' : diamonds, 'clubs': clubs, 'spades': spades}

    round_score = 0
    suit = random.randint(0,3)
    suit_val = deck.keys()[suit]
    suit_1 = random.randint(0,3)
    suit_val_1 = deck.keys()[suit_1]

    card = random.randint(0,12)
    card_val = deck.values()[suit][card]
    card_1 = random.randint(0,12)
    card_val_1 = deck.values()[suit_1][card_1]

    print "you drew a %s of %s and %s of %s" % (card_val, suit_val, card_val_1, suit_val_1)
    if(card_val in ('K','Q','J')):
        round_score += 10
        del deck[suit_val][card]
    elif(card_val=='A'):
        round_score+=1
        del deck[suit_val][card]
    else:
        round_score+= int(card_val)
        del deck[suit_val][card]


    if(card_val_1 in ('K','Q','J')):
        round_score += 10
        del deck[suit_val_1][card_1]
    elif(card_val=='A'):
        round_score+=1
        del deck[suit_val_1][card_1]
    else:
        round_score+= int(card_val_1)
        del deck[suit_val_1][card_1]

    print "your initial round score is %i" %round_score

    time.sleep(1)

    while round_score<=21:
        play_on = raw_input("Would you like to hit again or stay?")
        time.sleep(1)
        if(play_on.lower() == 'stay'):
            return round_score
            break
        suit = random.randint(0,3)
        suit_val = deck.keys()[suit]
        card = random.randint(0,len(deck[suit_val_1])-1)
        card_val = deck.values()[suit][card]

        if(card_val in ('K','Q','J')):
            round_score += 10
            del deck[suit_val][card]
        elif(card_val=='A'):
            round_score+=1
            del deck[suit_val][card]
        else:
            round_score+= int(card_val)
            del deck[suit_val][card]

        print "you drew a %s of %s" % (card_val, suit_val)

        if round_score>21:
            print "You busted with a score of %i" % (round_score)
            return round_score
            break
        print "you have a score of %i" %(round_score)
        time.sleep(1)
game_21()
