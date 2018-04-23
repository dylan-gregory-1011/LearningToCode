#!/usr/bin/env python
"""finished on 7/6/2017: A text file of Roman Numerals were givenself.
Some numbers can be written by more than one roman numeral although there is only one
most efficient roman numeral for each number.

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

file_path_for_roman_numerals = '\\PATH\\TO\\FILE\\Finished_Project_txts\\p089_roman.txt'

def calculateOptimalRomanNumeralFor(number):
    #create a dictionary with the values that are associated with each. Also create an array
    #to allow the cycle to iterate through in numerical order.
    roman = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1, 'IV': 4, 'IX': 9, 'XL':40, "XC": 90, 'CD': 400, 'CM':900}
    roman_order = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    #initialize the optimized roman numeral
    optimized_roman = ''
    ix = 0
    #create a while loop that exits when the number has been reduced to zero (This means
    #that all the values have been added to the roman numeral)
    while number>0:
        roman_number = roman[roman_order[ix]]
        if roman_number <=number:
            number -= roman_number
            optimized_roman += roman_order[ix]
            continue
        ix+=1
    return optimized_roman

def calculateNumberFromRomanNumeral(numeral):
    #create a dictionary that has the values per the roman numerals.
    roman = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
    number= 0
    #iterate over the values in the string.  If the value of the future numeral is greater
    #then the current value then subtract the current value
    #if it isnt, add the roman numeral's value to the number
    for dig in xrange(0,len(numeral)):
        try:
            if roman[numeral[dig+1]]> roman[numeral[dig]]:
                number -=  roman[numeral[dig]]
                continue
        except IndexError:
            pass
        number+= roman[numeral[dig]]
    return number

if __name__ == '__main__':
    roman = []
    with open(file_path_for_roman_numerals , 'r') as p89:
        for line in p89:
            roman.append(line.replace("\n",""))
    new_roman = []
    for numeral in roman:
         new_roman.append(calculateOptimalRomanNumeralFor(calculateNumberFromRomanNumeral(numeral)))
    print len("".join(roman)) - len("".join(new_roman))
