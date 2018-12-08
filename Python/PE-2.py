# https://projecteuler.net/problem=2

fib1 = 0
fib2 = 1
_sum = 0

while fib1 < 4000000:
    fib1, fib2 = fib2, fib1 + fib2
    if fib1 % 2 == 0:
        _sum += fib1

print(_sum)
