from binomaial_reps import binomial_calc
#instead of the below method, run a binomial calculation that is (n+n)!/(n!+n!).  This is because we can move in two different ways
#much quicker then the below method
size = 20
binomial_calc(size*2,size)
#this function is applicable for all values, but it takes too long to solve for larger values.
#for each previous position, create two new paths, one going up by one value and one going sideways
def increment(position):
    i = 0
    move_forward = 0
    new_array = []
    while i<2:
        prev_position = position[:]
        #if one of the positions is 0, then only increment the value that is != 0
        if prev_position[i]!=0:
            prev_position[i]= prev_position[i] - 1
            new_array.append(prev_position)
            move_forward = 1
        i+=1
    return new_array

extrap_further = 1
move_array = [[11,11]]
#start at the final position and move back towards the start
#if all the values are 0 then you are done
while extrap_further>0:
    extrap_further = 0
    next_position = []
    #call the increment step and create a new array with all of the new locations
    for array in move_array:
        new_array = increment(array)
        for new_pos in new_array:
            next_position.append(new_pos)

    move_array = next_position[:]
    extrap_further = 0
    #check to see if we are finished
    for pos in move_array:
        if sum(pos) !=0:
            extrap_further = 1
            break

print move_array
print len(move_array)
