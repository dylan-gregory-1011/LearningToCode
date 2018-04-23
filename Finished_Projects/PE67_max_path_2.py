#finished on 6/19/2017
def main():
    maximum_path = []
    #open the text file and download the numbers
    with open('C:\\Users\\dylan smith\\Documents\\Python\\Project_Euler\\p067_triangle.txt') as triangle:
        for row in triangle:
            row = row.strip('\n').split(' ')
            new_row = [int(x) for x in row]
            maximum_path.append(new_row)

    #cycle through each row in the sheet
    for x in xrange(1,len(maximum_path)):
        #cycle through each number in the row.  If the number is the first or last number, increment the total by the value of the previous number
        #if the value is somewhere inbetween then check to see which of the previous numbers is larger and increment that one.
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



main()
