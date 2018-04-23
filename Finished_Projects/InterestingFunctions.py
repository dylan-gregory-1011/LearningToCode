from random import sample
import sys
def millerRabinTestForPrimality(n, k = 7):
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
    # should be faster than n % 2..... bitwise operator
    if n & 1 == 0:
       return False

    d,r = n-1, 0
    while d & 1 == 0:
        #d >> 1 (is the same as d//2^1)
        r, d = r + 1, d >> 1
    #the sample function: sample(population,k), returns k values that are randomly spread over the range listed.
    #it returns a k list of samples from the population.  For this we also use the min function to limit values
    for a in sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
        #use the power function to optimally calculate the new x
        x = pow(a,d,n)
        if x != 1 and x != n - 1:
            for s in xrange(1,r):
                x = pow(x,2,n)
                if x == 1:
                    return False
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False
    return True

#this uses frequency analysis on the cipher.
#iterate over the cipher in ranges of 3 and get the most common values for each position
def getKey(cipher, sizeKey) :
    freqNumInABC = [{}, {}, {}]
    key = [0 for i in range(sizeKey)]
    for i in range(sizeKey) :
        maxValue = 0
        for j in range(i, len(cipher), 3) :
            if cipher[j] in freqNumInABC[i] :
                freqNumInABC[i][cipher[j]] += 1
            else :
                freqNumInABC[i][cipher[j]] = 1
            if freqNumInABC[i][cipher[j]] > maxValue :
                maxValue = freqNumInABC[i][cipher[j]]
                key[i] = cipher[j]
    for i in range(sizeKey) :
        key[i] = key[i] ^ ord(' ')
    return key


#######Permutations!
#create a string of all the numbers arranged in order.  This will be used to check for permutations
def rearrangePermutation(number):
    return ''.join([str(y) for y in sorted([int(x) for x in str(number)])])
#returns true if the value is a permutation of the other, else returns false.
def checkIfPermutation(numberOne, numberTwo):
    if rearrangePermutation(number) == rearrangePermutation(numberTwo):
        return True
    else:
        return False

#define a function that creates the reverse number of the inputted number.  Makes it a string and then flips all the numbers
def createOwnPalindrome(number):
    numStr = str(number)
    #palindrome = ''
    palindrome = int(''.join([num_str[x-1] for x in range(len(num_str),0, -1)]))
    return palindrome


#binary search allows the user to search through a sorted array quicker then normal.  It splits the
#array in half and checks to see if the value at the midpoint is larger or smaller then the value we
#are searching for.  Once it figures this out it isolates this half of the array and searches this.
def binarySearch(anArray, item):
    first = 0
    last = len(anArray)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if anArray[midpoint] == item:
            found = True
        else:
            if item < anArray[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    #this search returns either true if the value exists or false if the value doesnt
    return found
