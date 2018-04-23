#import the counter that checks to get distinct values for card counts
from collections import Counter
#calculates the best possible score that each players hand has dealt them
def get_best_cards(hand):
    #initialize the cards hand as well as the suit to check if it is flush
    cards = []
    suits = hand[1]
    s_mat = 1
    #get an array of face values when i = 0 and check to see if it is a flush when i = 1
    for i in range(2):
        #get the five face values and convert the face cards to values
        for h in xrange(i,len(hand), 2):
            if i ==0:
                if hand[h] == 'T':
                    card = 10
                elif hand[h] == 'J':
                    card = 11
                elif hand[h] == 'Q':
                    card = 12
                elif hand[h] == 'K':
                    card = 13
                elif hand[h] == 'A':
                    card = 14
                else:
                    card = hand[h]
                cards.append(int(card))
            #when the suit matches the previous suits then continue to check the suit.  If it doesnt match it can't be a flush
            if i == 1 and h >1:
                if suits == hand[h]:
                    continue
                else:
                    s_mat = 0
                    break
    #sort the cards by value
    cards.sort(reverse = True)
    for i in range(len(cards)):
        try:
            #if the cards are all continuous then it is a straight, if not break
            if cards[i]-cards[i+1] ==1:
                continue
            else:
                break
        #if we make it all the way through the array then it is a straight.  Return either a royal flush if it starts
        #with an ace. Return straight flush if it doesnt, else return just a straight if it isnt a flush
        except IndexError:
            if s_mat == 1:
                if cards[0] == 14:
                    #print "royal flush"
                    return 10
                else:
                    #print "straight flush"
                    return 9 - 1/float(cards[0])
            else:
                #print "straight"
                return 5 -1/float(cards[0])
    #get a dictionary with all the distinct card values as well as their count
    counter =  Counter(cards)
    #if the length of counter is 2 it is either a four of a kind or a full house
    #check to see if the count of the most common card is 4.  If it isnt its a full house
    if len(counter) == 2:
        if counter.most_common()[0][1] == 4:
            #print 'four of a kind'
            return 8 -1/float(counter.most_common()[0][0])
        else:
            #print "full house"
            return 7
    if s_mat == 1:
        #print 'flush'
        return 6
    #check to see if it a three of a kind
    if counter.most_common()[0][1]  == 3:
        #print 'three of a kind'
        return 4 -1/float(counter.most_common()[0][0])
    #if the most common counter is 2 then it is either a pair of twos or two of a kind. If the len of the counter is 3 then it is two of a kind
    elif counter.most_common()[0][1] ==2:
        if len(counter) == 3:
            #print 'two pairs'
            return 3 -1/float(counter.most_common()[0][0])
        else:
            #print 'two of a kind'
            return 2 -1/float(counter.most_common()[0][0])
    else:
        #print "high card"
        return 1 -1/float(cards[0])

def main():
    #import the text file and seperate the hands.  Be sure to get rid of the spaces as well as the new line delimiters
    all_hands = []
    with open('\\PATH\\TO\\FILE\\p054_poker.txt' , 'r') as p54:
        for line in p54:
            all_hands.append(line.replace(" ","").replace("\n",""))
    #set the win count at 0 and increment over all the hands.
    win1 = 0
    for card_round in all_hands:
        #get the hand for player one and player two.
        hand1 = card_round[:10]
        hand2 = card_round[10:]
        #if player 1 has a better hand then player two he/she wins.  if not, player two wins
        #applied a numerical value to each of the possible outcomes and incremented each value by a fraction based on the card that was in play
        if get_best_cards(hand1) > get_best_cards(hand2):
            win1+=1
    print win1

#run the function
main()
