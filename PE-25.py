'''

def fib(n):
	if n == 1 or n == 2:
		return 1

	f_1 = 0
	f_2 = 1
	f_3 = 0
	a = 1

	while a < n:
		f_3 = f_1 + f_2
		f_1 = f_2
		f_2 = f_3
		a += 1

	return f_3


i = 1

while len(str(fib(i))) != 1000:
	i += 1

print(i)'''

fib_memo = {}

def fib(n):
    if n <= 2:
        return 1
    else:
        if n not in fib_memo:
            fib_memo[n] = fib(n - 1) + fib(n - 2)
        return fib_memo[n]


i = 1

while len(str(fib(i))) != 1000:
	i += 1

print(i)
