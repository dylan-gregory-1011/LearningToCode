i = 1
#begin the list array with zero
list_array = ['0']
#get the pandigital numbers including 0-9
#we first start with an array that is of '0' and work our way out
total_array = []
while i<10:
    new_list_array = []
    #for every number we will create an array of all the panditigal numbers, Working recursively from 0
    for pandigital in list_array:
        #create an array with the appended at the very beginning and all the values get added to the end
        new_list_array.append(str(i)+pandigital)
        new_list_array.append(pandigital + str(i))
        j = 1
        #we then create array entries that add the number to all points in the middle of the arrays
        while j<len(pandigital):
            new_list_array.append(pandigital[:j]+str(i)+pandigital[j:])
            j+=1
    list_array = new_list_array
    i+=1
print 'permutations created'
#change all the values to integers using list comprehension
num_array = [int(num) for num in list_array]
print 'Changed to integers'
num_array_sort = num_array.sort()
print num_array[999999]
