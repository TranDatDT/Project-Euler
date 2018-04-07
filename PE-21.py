import math


def sum_of_divisors(n):
    total = 0

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i + n // i

        if i ** 2 == n:
            total -= i

    return total - n


number = 2
amicable_sum = 0

while number < 10000:
    temp = sum_of_divisors(number)

    if temp == number or temp >= 10000:
        number += 1
        continue

    if sum_of_divisors(temp) == number:
        amicable_sum += number

    number += 1

print(amicable_sum)
