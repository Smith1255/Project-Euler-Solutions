#Andrew Smith
#December 30 2013
total = 0
a = 1
b = 1

while b < 4000000:
	a, b = b, a + b

	if a % 2 == 0:
		total = total + a
print total
