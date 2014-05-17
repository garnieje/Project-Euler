# Problem 293

# An even positive integer N will be called admissible, if it is a power of 2 or its distinct prime factors are consecutive primes.
# The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

# If N is admissible, the smallest integer M > 1 such that N+M is prime, will be called the pseudo-Fortunate number for N.

# For example, N=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7.
# The next prime number after 631 is 641; hence, the pseudo-Fortunate number for 630 is M=11.
# It can also be seen that the pseudo-Fortunate number for 16 is 3.

# Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N less than 109.


import pyprimes
import math
n = 23 
limit = math.pow(10, 9) 

# generate the list of prime below 23
# no need to get prime greater than 23 here
primes = pyprimes.primes_below(n)
primeList = []
for i in primes:
    primeList.append(i)

# function check whether a number is admissible
def check(cour):
    factor = set()
    d = 2
    n = cour
    while n > 1:
        while n%d == 0:
            factor.add(d)
            n /= d
        d += 1

        if d*d > n:
            if n > 1:
                factor.add(n)
                break
    maxi = max(factor)
    liste = pyprimes.primes_below(maxi)
    for i in liste:
        if not(i in factor):
            return(False)
    return(True)
            
    
# set which would contain the pseudo fortunate number found
global pseudofortunate
pseudofortunate = set()

def pe293(primeList, cour, limit):
    if len(primeList) == 0:
        if cour>limit:
            return(0)
        else:
            # look for the pseudo fortunate number associated
            M = 2
            while not(pyprimes.isprime(cour + M)):
                M += 1
            if not M in pseudofortunate:
                pseudofortunate.add(M)
                return(M)
            else:
                return(0)                
    else:
        count = 0
        while cour <= limit:
            # check if the number is admissible before doing the recursion
            if check(cour):
                count += pe293(primeList[1::], cour, limit)
                cour *= primeList[0]
            else:
                break
        return(count)

print(pe293(primeList, 2, limit))
