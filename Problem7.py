"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def nth_prime_number(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime number generated
    return prime_list[-1]

print(nth_prime_number(10_001))