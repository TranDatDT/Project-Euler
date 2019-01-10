'''A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers'''


li = []
max_number = -1
for numb1 in range(999, 0, -1):
    for numb2 in range(999, 0, -1):
    	mul = numb1 * numb2
        if str(mul) == str(mul)[::-1]:
            if max_number < mul:
            	max_number = mul

print(max_number)
