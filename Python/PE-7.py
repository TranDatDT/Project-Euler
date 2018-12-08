'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?'''


import math


def is_prime(n):
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


i = 3
count = 1

while True:
    if is_prime(i):
        count += 1

    if count == 10001:
        print(i)
        break

    i += 2
