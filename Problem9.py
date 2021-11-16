""""
Project Euler
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


"""
1. Find three numbers that are less than 1000
2. The first two numbers must each equal in a pythagorean triplet.
      2a. a**2 + b**2 = c**2
3. Each number is smaller than the next. a < b < c
4. The answer asks for the product of abc, which means to multiply a * b * c and print the result
"""
# loop from 1 to 400 in a and b
# subtract a and b from 1000 to get c
# check to see if a < b < c
# check to see if a**2 + b**2 = c**2
# that's the answer. Multiply it up
for a in range (1,400):
    for b in range(1,400):
        c = (1000 - a) - b

        if a < b < c:
            if a**2  + b**2 == c**2 :
                print(f"{a}^2 + {b}^2 = {c}^2")
                print(f"{a} * {b} * {c} = {a*b*c}")