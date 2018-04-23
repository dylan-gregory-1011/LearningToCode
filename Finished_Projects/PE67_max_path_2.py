#!/usr/bin/env python
"""finished on 6/19/2017: Gets the maximum value returned from a triangle path
that is laid out in the text file

Cycle through each number in the row.  If the number is the first or last number,
increment the total by the value of the previous number if the value is somewhere in 
between then check to see which of the previous numbers is larger and increment that one.
"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

file_path = '\\PATH\\TO\\FILE'

def getTriangleFromFile(file_path):
    with open(file_path + 'p067_triangle.txt') as triangle:
        for row in triangle:
            row = row.strip('\n').split(' ')
            new_row = [int(x) for x in row]
            maximum_path.append(new_row)
    return maximum_path
if __name__ == '__main__':
    maximum_path = getTriangleFromFile(file_path)

    #cycle through each row in the sheet
    for x in xrange(1,len(maximum_path)):
        for y in xrange(0,len(maximum_path[x])):
            if y == 0:
                maximum_path[x][y] += maximum_path[x-1][y]
            elif y == len(maximum_path[x])-1:
                maximum_path[x][y] += maximum_path[x-1][y-1]
            else:
                if maximum_path[x-1][y]>= maximum_path[x-1][y-1]:
                    maximum_path[x][y]+=maximum_path[x-1][y]
                else:
                    maximum_path[x][y]+=maximum_path[x-1][y-1]

    print max(maximum_path[len(maximum_path)-1])
