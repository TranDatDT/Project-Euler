'''What is the value of the first triangle number to have
over five hundred divisors?'''


import math


number = 0
i = 0

while True:
	count = 0

	for j in range(1, int(math.sqrt(number) + 1)):
		if number % j == 0:
			count += 2
		if j ** 2 == number:
			count -= 1
	
	if count >= 500:
		break

	number += i
	i += 1

print(number)
