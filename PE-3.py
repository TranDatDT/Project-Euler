# https://projecteuler.net/problem=3


def max_prime(n):
    d = 2
    while n > 1:
        while n % d == 0:
            n = n // d  # n is integer
        d += 1
    return d - 1


def main():
    print(max_prime(600851475143))


if __name__ == '__main__':
    main()
