import math


def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == 1:
                divisors.append(i)
            else:
                divisors.append(n//i)
                divisors.append(i)

        if i * i == n:
            divisors.remove(i)

    return divisors


abundant_numbers = []

for i in range(12, 28123):  # because 12 is the smallest abundant number
    if sum(find_divisors(i)) > i:
        abundant_numbers.append(i)

total = 1

for number in range(2, 28123):
    check = True

    for abundant in abundant_numbers:
        if abundant < number:
            if number - abundant in abundant_numbers:
                check = False
                break
        else:
            break

    if check is True:
        total += number

print(total)
