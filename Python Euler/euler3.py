from time import time
from math import sqrt
x = int(raw_input("Enter any value to find it's largest prime factor: "))

a = time()
i = 2

def is_prime(x):
	y = 3

	if (x % 2 == 0) and (x != 2):
		return False
	while y < sqrt(x): #factor will never be larger than sqrt.
		if x % y == 0:
			return False
		y += 2
	return True
#end is prime

#if is_prime(x):
	#print "Error, no factors"
largest = 0
i = 3
xSqrRoot = sqrt(x)

while i < xSqrRoot:
	if x % i == 0:
		if is_prime(i):
			largest = i
	i += 2
print largest
b = time()
print b - a
print "PING!"
