'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    
    elif n == 0 or n == 1:
        return False

    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

    return True


print(sum(i for i in range(3, 2000000, 2) if is_prime(i)) + 2)