'''2520 is the smallest number that can be divided
by each of the numbersfrom 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''
import math


def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def main():
    prime_number = []
    prime_number_max = []

    for i in range(2, 21):
        if is_prime(i):
            prime_number.append(i)

    max_exponent = 0

    for i in range(20//2 + 1):
        if prime_number[0] ** i < 20:
            max_exponent = i

    while len(prime_number) > 0:
        if prime_number[0] ** max_exponent < 20:
            prime_number_max.append(prime_number[0] ** max_exponent)
            prime_number.remove(prime_number[0])

        else:
            max_exponent = max_exponent - 1

    smallest_multiple = 1

    del prime_number

    for i in prime_number_max:
        smallest_multiple = smallest_multiple * i

    print(smallest_multiple)


if __name__ == '__main__':
    main()
