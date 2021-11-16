"""

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600_851_475_143 ?

"""

import math

def primeFactors(n):
    while n % 2 == 0:
        print (2)
        n = n / 2
    # n must be odd at this point
    for i in range (3, int(math.sqrt(n))+1,2):
        #while i divides n, print i and divide n
        while n % i == 0:
            print (i)
            n = n / i
    if n > 2:
        print (n)

primeFactors(600851475143) 