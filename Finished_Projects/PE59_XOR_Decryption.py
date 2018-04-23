
#create a decode function that iterates through the list of ascii values and uses the correct place of the key.
def decode(key, cipher,words):
    i = 0
    check = 0
    decode = ''
    len_key = len(key)
    key_array = [ord(x) for x in key]
    #go over each value from the file and convert each value back to a character
    for x in cipher:
        #if i = 3 then reset i to 0 and iterate over the key again
        if i == len_key:
            i = 0
        #decode the value into a character using the correct key code
        decode +=chr(x^key_array[i])
        #once decode is greater then 40 characters, check to see if there are any words present.  If not,break and move on to next public key
        if len(decode)>40 and check == 0:
            check = 1
            if [x for x in words if x.lower() in decode.lower()]:
                i+=1
                continue
            else:
                decode = 'balls'
                break
        i+=1
    return decode

#get the sum of all the values.  Once we have the key, sum the ascii values for all the words.
def decode_sum(key,cipher):
    i = 0
    decode = 0
    key_array = [ord(x) for x in key]
    len_key = len(key)
    for x in cipher:
        if i == len_key:
            i = 0
        decode +=x^key_array[i]
        i+=1
    print decode

#as we iterate through all of the key possibilities, use a function that calls every possible key value
def get_key(i,j,k):
    return key_array[i]+key_array[j]+key_array[k]

#here is the main function that iterates over the list of possible key values and tries to decode each values
#we get the key and then decode the key.  if the value returned is not equal to the failed value then it continues on
def main():
    key_array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    cipher_stg = []
    #download the file and replace each quotation mark with a blank space
    with open('\\PATH\\TO\\FILE\\p059_cipher.txt' , 'r') as p57:
        for line in p57:
            cipher_stg = line.split(',')
    cipher = [int(x) for x in cipher_stg]
    words = []
    #get a list of common words.  To improve performance could also use a smaller list of more common words
    with open('\\PATH\\TO\\FILE\\words.txt' , 'r') as words:
        for line in words:
            words = line.split(',')
    #limit the list to only include words with a length greater then 5 to not allow for false positives
    words_new = [x for x in words if len(x)>5]

    stop = 0
    for i in xrange(0,26):
        for j in xrange(0,26):
            for k in xrange(0,26):
                key = get_key(i,j,k)
                new_string = decode(key,cipher,words_new)
                if new_string!= 'balls':
                    print new_string
                    print key
                    stop = 1
                    break
            if stop == 1:
                break
        if stop == 1:
            break
    #get the sum of the ascii values
    decode_sum(key, cipher)
main()
