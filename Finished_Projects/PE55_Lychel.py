
#define a function that creates the reverse number of the inputted number.  Makes it a string and then flips all the numbers
def createReverse(number):
    numStr = str(number)
    #palindrome = ''
    palindrome = int(''.join([num_str[x-1] for x in range(len(num_str),0, -1)]))
    return palindrome

print create_Reverse(582)
#the main function initializes a count and then for loops over the x range between 1 and 10,000 to see if the numbers can be added
#to make a palindrome
def main():
    count = 0
    for i in xrange(1,10001):
        #reset the iterations to 1 each loop and make the lychel variable 1
        iterations = 1
        lychel = 1
        new_sum = i
        #while iterations<50 then continue to add the number to its reverse
        while iterations<50:
            #get the new sum
            new_sum = new_sum + createReverse(new_sum)
            str_num = str(new_sum)
            len_str_num = len(str_num)
            pali = 'Y'
            #check to see if the number is a palindrome.  It makes its way through the number
            #and if each position on the front and back match, continue through else not a palindrome and break
            for x in range(0,len_str_num ,1):
                if str_num[x] == str_num[len_str_num-1-x]:
                    continue
                else:
                    pali = 'N'
                    break
            if pali == 'Y':
                lychel = 0
                break
            iterations +=1
        #if lychel is still 1 then it is a lychel number.  Add to the count and continue
        if lychel == 1:
            count +=1
    print count
#main()
