numbers = ['1','2','3','4','5','6','7','8','9']
pandigits = []
num = 1
iterate = 'T'
#start at 1 and increment to 1 million
while num<1000000:
    pandig = ''
    n = 1
    clean = 'Y'
    #we make the pandigital string as null at fist and then continue to concatenate the values through every iteration
    while len(pandig)<9:
        new_num = n*num
        pandig = pandig+str(new_num)
        n+=1
    #if n>9 then we move on to the next number
    if len(pandig)!=9:
        num+=1
        continue
    #if the number is not in the array of numbers then it is not clean and we break to the next number.
    for dig in numbers:
        if dig not in pandig:
            clean = 'N'
            break
    if clean == 'Y':
        pandigits.append(int(pandig))
        print num
    num +=1
print pandigits
print max(pandigits)
print sum(pandigits)
