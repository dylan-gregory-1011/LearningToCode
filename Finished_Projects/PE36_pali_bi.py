#finished on 6/19/2017

#this function inserts numbers into arrays and allow for the quick production of palindromes.  It decides whether there needs to be a single inserts
#or a double insert and then adds the new numbers to the middle.  returns a new arrays
def insert_numbers(prev_array , add):
    index_pos = len(prev_array[0])/2
    sub_array = []
    if add == 1:
        sub_array.append([arr[:index_pos]+ str(x)+ arr[index_pos:] for x in xrange(0,10) for arr in prev_array])
        array = [item for sublist in sub_array for item in sublist]
    else :
        sub_array.append([arr[:index_pos]+ str(x)+ str(x) +arr[index_pos:] for x in xrange(0,10) for arr in prev_array])
        array = [item for sublist in sub_array for item in sublist]
    return array

#dec to bin takes a decimal value and converts it to a binary value
def dec_to_bin(x):
    return bin(x)[2:]

def createListOfPalindromes():
        #declare all initial arrays as well where the values are null for the more complex arrays and filled in for simplicity for the single and double
        single = ['1','2','3','4','5','6','7','8','9']
        double = ['11','22','33','44','55','66','77','88','99']

        #fill the arrays with the different number lengths calling the insert numbers function appropriately.  Then add to one big array
        triple = insert_numbers(double,1)
        quad = insert_numbers(double,2)
        quin = insert_numbers(quad,1)
        sext = insert_numbers(quad,2)
        full_list = single+ double + triple + quad + quin + sext
        return full_list

def main():
    full_list = createListOfPalindromes()
    #initialize the sum and iterate over all the palindromes.  First call the binary number for each palindrome and then check to see if the binary
    #number is a palindrome.  If the palindrome flag stays 1, the value is a double palindrome and increment the sum by this number
    sum_numbers= 0
    for pali in full_list:
        bin_num = dec_to_bin(int(pali))
        palindrome = 1
        for x in xrange(0,len(bin_num)):
            if bin_num[x] == bin_num[len(bin_num)-x-1]:
                continue
            else:
                palindrome = 0
                break
        if palindrome == 1:
            sum_numbers+=int(pali)
    print sum_numbers
main()
