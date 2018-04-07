'''A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers'''


li = []
for numb1 in range(999, 0, -1):
    for numb2 in range(999, 0, -1):
        if str(numb1 * numb2) == str(numb1 * numb2)[::-1]:
            li.append(numb1 * numb2)

print(max(li))
