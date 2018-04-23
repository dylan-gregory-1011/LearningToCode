#define a pattern, start the count at 1 and the sum at 1 and follow the pattern of incrementing the count by the current number
#(2,4,6,8) and then adding that number to the sum
def main():
    init_count = 1
    init_sum = 1
    x_by_x = 3
    increment = 2
    while x_by_x<=1001:
        for x in xrange(0,4):
            init_count+=increment
            init_sum+=init_count
        increment+=2
        x_by_x+=2
main()
