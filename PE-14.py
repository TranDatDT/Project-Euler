current = 0
high = 0


def collatz(i):
    counter = 1
    while i > 1:
        counter = counter + 1
        if i % 2 == 0:
            i = i / 2
        else:
            i = 3*i + 1
    return counter


for i in range(1, 1000000):
    current = collatz(i)
    if current > high:
        high = current
        number = i

print(number)
