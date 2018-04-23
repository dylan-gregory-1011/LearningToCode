"""
When you are in class and can find anyone to play hangman with... Inspiring graphics to boot too.
"""
import random
HANGMANTEST = [1,2,3,4,5,6,7]
def hangman_graphic(guesses):
		if guesses == 0:
			print "________      "
			print "|      |      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 1:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|             "
			print "|             "
			print "|             "
		elif guesses == 2:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /       "
			print "|             "
			print "|             "
		elif guesses == 3:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|      "
			print "|             "
			print "|             "
		elif guesses == 4:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|             "
			print "|             "
		elif guesses == 5:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     /       "
			print "|             "
		else:
			print "________      "
			print "|      |      "
			print "|      0      "
			print "|     /|\     "
			print "|     / \     "
			print "|             "
			print "The noose tightens around your neck, and you feel the"
			print "sudden urge to urinate."
			print "GAME OVER!"
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
rand_Int = random.randint(0,len(words)-1)

guess_Word = words[rand_Int]
guess_Word_Array = []
my_guess_Array = []
error_Guess = []
i = 0
j = 0
guesses = 0

correct_Guess=0
prev_Guess = 0
guess = ''

while i <len(guess_Word):
    guess_Word_Array.append(guess_Word[i].upper())
    i+=1
while j <len(guess_Word):
    my_guess_Array.append('_')
    j += 1

letters_Left = len(guess_Word_Array)

hangman_graphic(guesses)
print my_guess_Array
guess = raw_input("What letter is your first guess? ").upper()
print "Remember, if you want to quit at any time guess GIVE UP"
while guesses<len(HANGMANTEST):
    if guess.upper() == 'GIVE UP':
        print 'The word you were looking for was %s' %(guess_Word)
        break
    k = 0
    g = 0
    while k< len(guess_Word):
        if guess.upper() == my_guess_Array[k]:
            prev_Guess = 1
            break
        if guess.upper() == guess_Word_Array[k]:
            my_guess_Array[k] = guess.upper()
            letters_Left-=1
            correct_Guess = 1
        k+=1
    while g < len(error_Guess):
        if guess.upper() == error_Guess[g]:
            prev_Guess = 1
            break
        g+=1
    if prev_Guess==1:
            hangman_graphic(guesses)
            print my_guess_Array
            print "your previous attempts are", error_Guess
            guess = raw_input("You already guessed that, what is your next guess ?")
            prev_Guess = 0
            continue
    if correct_Guess == 0:
        guesses +=1
        hangman_graphic(guesses)
        print my_guess_Array
		error_Guess.append(guess.upper())
        print "your previous attempts are", error_Guess
        if guesses==6:
            print "You lost... the word you were looking for was %s" %(guess_Word)
            break
        guess = raw_input("That is incorrect, what is your next guess? ")
        continue
    if correct_Guess ==1:
        correct_Guess=0
        hangman_graphic(guesses)
        print my_guess_Array
        print "your previous attempts are", error_Guess
        print letters_Left
        if letters_Left == 0:
            print "CONGRATS, YOU WON!!!!!"
            break
        guess = raw_input("Your guess was correct, what is your next guess? ")
