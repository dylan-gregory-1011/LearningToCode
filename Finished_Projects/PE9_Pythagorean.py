import math

a = 4
b = 5

c_integer = "N"
while a<500:
    c_integer = "N"
    b = a+1
    c = math.sqrt(a**2+b**2)
    if c.is_integer():
        c_integer = "Y"
    while a+b+c<1000:
        c_integer = "N"
        b+=1
        c = math.sqrt(a**2+b**2)
        if c.is_integer():
            c_integer = "Y"
    if a +b+int(c)==1000 and c_integer == "Y":
        "found"
        break
    a+=1

print a
print b
print c
print a*b*c
