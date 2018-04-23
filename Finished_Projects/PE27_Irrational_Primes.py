import csv

def int_wrapper(reader):
    for v in reader:
        yield map(int, v)
n = 999
def quad_primes(n, a, b):
    return n*n + n*a + b

primes  =[]
with open('\\PATH\\TO\\FILE\\primes.csv') as prime_list:
      reader = csv.reader(prime_list)
      reader = int_wrapper(reader)
      for row in reader:
          primes.append(row[0])

a = -999
n_max = 1
sol_max = 0
while a <1000:
    b = -999
    while b<1000:
        n = 0
        while 1== 1:
            sol = quad_primes(n,a,b)
            i = 0
            found = 'N'
            while primes[i]<=sol:
                if sol == primes[i]:
                    found = 'Y'
                    break
                i+=1
            if found == 'N':
                break
            n+=1
        if n>n_max:
            n_max = n
            sol_max= a*b
        b+=1
    a+=1
print sol_max
print n_max
