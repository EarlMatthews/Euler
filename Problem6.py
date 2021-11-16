from functools import reduce

def square(x):
    return x*x

upper_bound = 100

sum_of_squares = sum(square(i) for i in range(1,upper_bound + 1))
square_of_sum = square(sum(range(1,upper_bound + 1)))
print(sum_of_squares)
print(square_of_sum)
print (square_of_sum - sum_of_squares)