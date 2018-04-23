#declare a list of all primes below 100
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

#check dictionary function is used when calculating the prime factors of each number 2<=a<=99.  This either adds one to the value of a prime factors
#if there is more then one or creates a new dictionary value if it is the first time the prime factor has been found
def check_dict(curr_dict, new_val):
    if new_val in curr_dict.keys():
        curr_dict[new_val] += 1
    else:
        curr_dict[new_val] = 1
    return curr_dict

#main function gets the number of distict values that this power calculation has created for a,b 2<=99
def main():
    #create an array of dictionaries that has the key of a prime number and a value of the number of times the prime is multiplied
    distinct_powers = []
    #this first for statement gets all of the base numbers between 2 and 99.  The componenets dictionary is a key (prime number), value(number of times used)
    #pair.  We set a_stg as a working value and work our way through the primes list and add values when we find a combination of a_stg modulo a prime = 0
    for a in xrange(2,101):
        components = {}
        a_stg = a
        while a_stg not in primes:
            for x in primes:
                if a_stg % x == 0:
                    components = check_dict(components, x)
                    a_stg = a_stg/x
                    break
        #add the last prime value to the list
        components = check_dict(components, a_stg)
        #copy the components into a working update dictionary.  Using the copy function makes a physical copy and not a pointer
        new_dict = components.copy()
        #this for statement works its way through the 99 powers, incrementing each prime value by the initial count each time (for the number 4,
        #each iteration increments the 2 value by 2).  With the new value, check if it is in the array of distinct powers, and if it isnt, append it.
        for b in xrange(2,101):
            for key in new_dict:
                new_dict[key]+= components[key]
                if new_dict not in distinct_powers:
                    distinct_powers.append(new_dict.copy())

print len(distinct_powers)
