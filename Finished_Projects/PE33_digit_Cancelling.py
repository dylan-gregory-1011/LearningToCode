import re
from numpy import isclose
denom = 12
denomonator = []
numerator = []
#work through all combinations of the numerator and denomonator
while denom<100:
    numer = 11
    #if the denomenator is modulo 10 then we skip this value as it would be trivial
    if denom%10 == 0:
        denom+=1
        continue
    #while the numerator is less then the denomenator we check to see if we can "cancel" any digits and if so we calculate the new fraction
    while numer < denom:
        value = float(numer) / float(denom)
        numer_str = str(numer)
        denom_Str = str(denom)
        i = 0
        if numer %10 == 0:
            numer +=1
            continue
        #iterate over both the digits in each the numerator and denomenator and delete them in both if they are found in both
        while i <2:
            j = 0
            while j<2:
                if denom_Str[i] == numer_str[j]:
                    denom_new = denom_Str.replace("%s" % denom_Str[i], '' )
                    numer_new = numer_str.replace("%s" % numer_str[j], '' )
                    if len(numer_new) == 0:
                        numer_new = numer_str[j]
                    if len(denom_new)== 0:
                        denom_new = denom_Str[i]
                    new_value = 0.00
                    new_value = float(numer_new)/float(denom_new)

                    if isclose(new_value, value, rtol=1e-04, atol=1e-04):
                        denomonator.append(denom)
                        numerator.append(numer)
                    break
                j+=1
            i+=1
        numer+=1
    denom+=1

print numerator
print denomonator
