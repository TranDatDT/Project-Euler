'''The prime factors of 13195 are 5, 7, 13, 29.
What is the largest prime factor of the number 600851475143?'''


def max_prime(n):
    d = 2

    while n > 1:
        while n % d == 0:
            yield d
            n = n // d

        d += 1


def main():
    print(max(list(max_prime(600851475143))))


if __name__ == '__main__':
    main()
