'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

_str = str(2**1000)

total = 0

for i in _str:
    if i == '0':
        continue

    else:
        total += int(i)

print(total)