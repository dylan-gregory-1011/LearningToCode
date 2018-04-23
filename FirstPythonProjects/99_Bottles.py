"""
To output all of the lyrics to the confusing song of 99 Bottles of beer on the wall.
"""
i = 99
j = 98
while i>2:
    print "%i bottles of beer on the wall, %i bottles of beer, take one down, pass it around, %i bottles of beer" % (i, i, j)
    i-=1
    j-=1

print "%i bottles of beer on the wall, %i bottles of beer, take one down, pass it around, %i bottle of beer" % (i, i, j)
i-=1
j-=1

print "%i bottle of beer on the wall, %i bottle of beer, take one down, pass it around, and youre drunk" % (i, i)
