#finished on 1/9/2018

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

#used to create an array of pentagonal numbers at the beginning
def pentagonalNumbers(n):
    return n*(3*n - 1) / 2

def arrayPentagonalSearch(anArray, minDifference):
    #this function goes through the array and searches to see if two values add up to the last value in the array.
    #if a value is found then the function then checks to see if the difference between those two values is also in the arrayLength
    #if this is true then it re-sets the min difference.  The function also exits if the difference we are calculating for becomes negative
    arrayLength = len(anArray)
    lastValue = anArray[len(anArray) - 1]
    for index, item in enumerate(anArray[-2::-1]):
        if 2*item - lastValue <=0:
            break
        if binarySearch(anArray, lastValue - item):
            if binarySearch(anArray, 2*item - lastValue):
                minDifference =  2*item - lastValue
                break
        if lastValue - item > minDifference:
            break
    return minDifference

def createPentagonalArray(n):
    #this function creates an array of pentagonal numbers of length n
    pentagonalArray = []
    for ix in xrange(n):
        pentagonalArray.append(pentagonalNumbers(ix + 1))
    return pentagonalArray


def main():
    #we iterate over the pentagonal array to check to see if the condition is met and re-set the min difference.
    pentagonalIX = 3
    minDifference = 100000000

    arrayOfPentagons = createPentagonalArray(10000)
    lengthPentagons = len(arrayOfPentagons)

    while (arrayOfPentagons[pentagonalIX] - arrayOfPentagons[pentagonalIX - 1]) < minDifference:
        minDifference = arrayPentagonalSearch(arrayOfPentagons[:pentagonalIX], minDifference)
        pentagonalIX +=1
        if pentagonalIX == lengthPentagons:
            break
    print minDifference

main()
