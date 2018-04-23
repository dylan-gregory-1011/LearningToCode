import math
#project169


def powers_init(max_num):
    values0 = []
    i = 0
    while sum(values0)<= max_num:
        i=1
        a = 2
        while sum(values0) +a <= max_num:
            i+=1
            a = math.pow(2,i)
        a = math.pow(2,i-1)
        values0.append(a)
        if sum(values0) == max_num:
            break
    return values0

def play_2048(max_num):
    values = []
    values = powers_init(max_num)
    count =1
    i = len(values)-1
    print values
    value_new = 0
    while i>=0:
        j = i
        k = i
        values = powers_init(max_num)
        value_new = values[i]/2
        del values[i]
        values.append(value_new)
        values.append(value_new)
        values.sort(reverse = True)
        value_check = values[i]
        while value_check == values[j+1]:
            try:
                if value_check == values[j+2]:
                    k = j+2
                    j = k
                    value_new = values[k]/2
                    del values[k]
                    values.append(value_new)
                    values.append(value_new)
                    values.sort(reverse = True)
                    continue
            except IndexError:
                pass
            break
        print values
        count+=1
        k = len(values) - 1
        while k>i :
            j = k
            value_new = values[k]/2
            del values[k]
            values.append(value_new)
            values.append(value_new)
            values.sort(reverse = True)
            value_check = values[k]
            if value_check<1:
                break
            while value_check == values[j+1]:
                try:
                    if value_check == values[j+2]:
                        k = j+2
                        j = k
                        value_new = values[k]/2
                        del values[k]
                        values.append(value_new)
                        values.append(value_new)
                        values.sort(reverse = True)
                        continue
                except IndexError:
                    pass
                break
            if sum(values) == max_num:
                count +=1
                print values
            k-=1

        i-=1
    print count
play_2048(math.pow(10,2))
