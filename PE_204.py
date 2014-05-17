# Problem 204
# A Hamming number is a positive number which has no prime factor larger than 5.
# So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
# There are 1105 Hamming numbers not exceeding 108.

# We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
# Hence the Hamming numbers are the generalised Hamming numbers of type 5.

# How many generalised Hamming numbers of type 100 are there which don't exceed 109?


import pyprimes
import math
n = 100
limit = math.pow(10, 9)

# generate liste of prime numbers less than 100
primes = pyprimes.primes_below(n)
primeList = []
for i in primes:
    primeList.append(i)


def hammer(primeList, cour, limit):
    if len(primeList) == 0:
        if cour>limit:
            return(0)
        else:
            return(1)
    else:
        count = 0
        while cour <= limit:
            # recursion
            count += hammer(primeList[1::], cour, limit)
            cour *= primeList[0]
        return(count)

print(hammer(primeList, 1, limit))
    
