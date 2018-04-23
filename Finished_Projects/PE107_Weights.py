#!/usr/bin/env python
"""finished on 6/29/2017: Find the minimum weights in a network that still connect the matrix
Start with an empty matrix and add the new point that offers the minimum weight added.
This is done through checking index of the column in the matrix to find the minimum available point. Check all the values
available to the network at that time (all points that are connected) and find the new minimum value that adds
to the network.  Ensure that it isnt a min value that is adding to the same point and check to
see if there are any local mins.  Add the point to the attached matrix and continue

func calculateTotalMatrixWeight(matrix) -> Int : Find the total weight in the matrix

func calculateMinimumConnectedWeightInMatrix(matrix) -> int : Find the minimum connected sum of the matrix.  This
method is explained above.

"""

__author__ = "Dylan Smith"
__copyright__ = "Copyright (C) 2017 Dylan Smith"
__credits__ = ["Dylan Smith"]

__license__ = "Public Domain"
__version__ = "1.0"
__maintainer__ = "Dylan Smith"
__email__ = "-"
__status__ = "Development"

path_for_file_used = 'C:\\Users\\uscdxs92\\Documents\\Python\\Project_Euler\\Finished_Project_txts\\p107_network.txt'

def calculateTotalMatrixWeight(matrix):
    #calculate the total sum of the entire network.  Since each value occurs twice, divide this value by two
    total_sum = 0
    for x in xrange(0,len(matrix)):
        for y in xrange(0,len(matrix)):
            if matrix[y][x] == '-':
                continue
            total_sum+= int(matrix[x][y])
    return total_sum/2

def calculateMinimumConnectedWeightInMatrix(matrix):
    #initialize all the variables.  Set min_sum to a be zero, and begin with the first attached points
    minimum_sum_of_matrix = 0
    attached_points_in_network = [0]
    while len(attached_points_in_network)<len(matrix):
        #set a local minimum so that the algorithm will find smaller values
        y_min = 1000000

        #build the new "minimum weights" matrix
        for x in attached_points_in_network:
            for y in xrange(0,len(matrix)):
                if matrix[y][x] == '-':
                    continue
                int_val = int(matrix[y][x])
                if int_val< y_min and y not in attached_points_in_network:
                    y_min = int_val
                    new_x = x
                    new_y = y
        #after checking through all the values, take the point out of the matrix and increment the values
        #append the new network point to the network and move on.
        minimum_sum_of_matrix +=y_min
        matrix[new_x][new_y] = '-'
        matrix[new_y][new_x] = '-'
        attached_points_in_network.append(new_y)
    return minimum_sum_of_matrix

if __name__ == '__main__':
    cube = []
    #download the cube and make 40 arrays with len(array) = 40
    with open(path_for_file_used) as p107:
        for row in p107:
            row = row.strip('\t\n').split(',')
            cube.append(row)

    #get the total weight of the matrix
    total_matrix_weight = calculateTotalMatrixWeight(cube)

    #calculate the minimum weight
    minimum_sum_of_matrix = calculateMinimumConnectedWeightInMatrix(cube)

    print total_matrix_weight - minimum_sum_of_matrix
