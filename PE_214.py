#problem 214
# Let φ be Euler's totient function, i.e. for a natural number n, φ(n) is the number of k, 1 ≤ k ≤ n, for which gcd(k,n) = 1.

# By iterating φ, each positive integer generates a decreasing chain of numbers ending in 1.
# E.g. if we start with 5 the sequence 5,4,2,1 is generated.
# Here is a listing of all chains with length 4:
# 5,4,2,1
# 7,6,2,1
# 8,4,2,1
# 9,6,2,1
# 10,4,2,1
# 12,4,2,1
# 14,6,2,1
# 18,6,2,1

# Only two of these chains start with a prime, their sum is 12.

# What is the sum of all primes less than 40000000 which generate a chain of length 25?

import time
import math
import pyprimes

start = time.time()

limit = 40000000
chain = 25
Sum = 0

## sieve to generate the value of phi
phi = list(range(limit + 1))

for i in range(2, limit + 1):
    if phi[i] == i: # i is prime
        for j in range(i, limit + 1, i):
            phi[j] = int(phi[j]*(i - 1)/i)

# loop over the prime to determine which ones have an iterative chain of length 25
for p in pyprimes.primes_below(limit):
    cour = p - 1
    for i in range(2, chain):
        cour = int(phi[cour])
        if cour == 1 and i < chain - 1:
            break
        if cour == 1 and i == chain - 1:
            Sum += p

print(Sum)
end = time.time() - start
print('in %f sec' % end)
