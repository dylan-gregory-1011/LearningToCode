#!/usr/bin/env python
"""finished on 2/2/2018: Analyzed a Matrix to solve
the path that gives the minimum path.  Starting from (0,0), iterate
through all of the points in the matrix and append each value by the
value that is the smallest of the two possible points that could feed this point

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2018 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

text_file_used = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\Finished_Project_txts\\p081_matrix.txt'
#ierate through the text file and build an embedded array of the matrix.
def buildMatrixFromFile():
    maximum_path = []
    #open the text file and download the numbers
    with open(text_file_used) as triangle:
        for row in triangle:
            new_row = [int(x) for x in row.strip('\n').split(',')]
            maximum_path.append(new_row)

    return maximum_path
if __name__ == '__main__':
    #get the matrix from file.
    minimum_path_matrix = buildMatrixFromFile()

    size_of_matrix = len(minimum_path_matrix)
    for row in xrange(0,size_of_matrix):
        #cycle through each number in the row.  If the number is the first or last number, increment the total by the value of the previous number
        #if the value is somewhere inbetween then check to see which of the previous numbers is larger and increment that one.
        for col in xrange(0,size_of_matrix):
            if row == 0 and col == 0:
                continue

            if row == 0 and col > 0:
                minimum_path_matrix[row][col] += minimum_path_matrix[row][col-1]
            elif col == 0 and row>0:
                minimum_path_matrix[row][col] += minimum_path_matrix[row-1][col]
            else:
                if minimum_path_matrix[row-1][col]>= minimum_path_matrix[row][col-1]:
                    minimum_path_matrix[row][col] += minimum_path_matrix[row][col-1]
                else:
                    minimum_path_matrix[row][col] += minimum_path_matrix[row - 1][col]

    print minimum_path_matrix[len(minimum_path_matrix)-1][len(minimum_path_matrix)-1]
