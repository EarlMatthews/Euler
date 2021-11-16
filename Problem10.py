
"""
Problem 10.
Summation of Primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sieveOfEratosthenes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p*p <= n):
        # if prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            #Update all multiples of p
            for i in range(p*p, n+1, p):
                prime[i]= False
        p += 1

    sum = 0
    for p in range(2, n+1):
        if prime[p]:
            sum += p 
    return sum

if __name__ == '__main__':
    n = 2 * (10 ** 6)
    print(f"Sum of Primes below {n} is {sieveOfEratosthenes(n)}")
    