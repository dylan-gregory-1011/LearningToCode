#this function calculates the reverse palindrome and creates a number that is a mirror immage down the middle
def palindrome(pali):
    str_pali = str(pali)
    rev_pali = str_pali[2]+str_pali[1]+str_pali[0]
    return int(str_pali + rev_pali)

pali = 999
found = 'N'
#once we have the palindrome created we find the largest divisor of the number
while pali>100:
    number = palindrome(pali)
    i = 999
    while i>=100:
        if number%i==0:
            if number/i >999:
                i-=1
                continue
            found = 'Y'
            div = number/i
            break
        i-=1
    if found == 'Y':
        break
    pali -=1

print pali
