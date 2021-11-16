"""
1000-digit Fibonacci number
Show HTML problem content 
Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def numberOfDigits(num):
    return sum(map(int,str(num)))

next = 0                                    # next fib number
limit = 1000                                # upper limit on number of digits
first_fib = 0                               # The first and second fib numbers are defined as 0 and 1
second_fib = 1
total = 0                                   # hold on to the total
while numberOfDigits(next) < limit:     # Check first_fib + Second_fib instead of next since the value isn't calculated until next iter
    next = first_fib + second_fib           # and we dont want to go over
    first_fib = second_fib
    second_fib = next                       # second and next become first and send fib
    total += 1

print(next)
print(numberOfDigits(next))
print(total)