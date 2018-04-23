#finished on 6/27/2017
#function that gets the triangle number
def triangle(n):
    return n*(n+1)/2
#function that returns the pentagonal number
def pentagonal(n):
    return n*(3*n-1)/2
#function that returns the hexagonal number
def hexagonal(n):
    return n*(2*n-1)

def main():
    #initialize all the variables to the correct numbers
    tri = 3
    t = 2
    pent = 5
    p = 2
    hexag =6
    h = 2
    count = 0
    #iterate until we find the second number that reaches this condition
    while count<2:
        #reset the hexag variable
        hexag = hexagonal(h)
        #iterate the pentagonal number until it is not less, it either will become greater or be equal
        while pent < hexag:
            p+=1
            pent = pentagonal(p)
        #iterate the triangle number until it becomes larger or is equal to the hexagonal number
        while tri < hexag:
            t+=1
            tri = triangle(t)
        #if they are all equal, print the number and then increment the count
        if hexag == tri and hexag == pent:
            count +=1
            print hexag
        h+=1
