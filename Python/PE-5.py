'''2520 is the smallest number that can be divided
by each of the numbersfrom 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''
from math import gcd


def main():
    n = 20

    lcm = 1

    for number in range(2, n + 1):
        lcm = (lcm * number) // gcd(lcm, number)
    
    print(lcm)


if __name__ == '__main__':
    main()
