'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of
the squares of the first one hundred natural numbers
and the square of the sum.
'''


the_sum_of_the_square = 0
the_sum_of_numbers = 0

for i in range(1, 101):
    the_sum_of_the_square += i**2
    the_sum_of_numbers += i

the_square_of_the_sum = the_sum_of_numbers ** 2
print(the_sum_of_the_square - the_square_of_the_sum)
