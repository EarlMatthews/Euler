"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

from math import gcd
from math import sqrt
from functools import reduce

def lcm(a,b):
    return(a*b//gcd(a,b))

def primeFactors(n):
    while n % 2 == 0:
        print (2)
        n = n / 2
    # n must be odd at this point
    for i in range (3, int(sqrt(n))+1,2):
        #while i divides n, print i and divide n
        while n % i == 0:
            print (i)
            n = n / i
    if n > 2:
        print (n)

ans = reduce(lcm,range(1,10 + 1))
print(ans)
primeFactors(ans)