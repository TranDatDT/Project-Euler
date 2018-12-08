# https://projecteuler.net/problem=1

sum_ = 0

for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        sum_ += number

print(sum_)
