import math 
counter = 333
c = []
a = 1
b = 2
check = 0
def isWhole(x):
	if x % 1 == 0:
		return True
	else: 
		return False

while counter < 998:
	c.append(counter ** 2)
	counter += 1
while b < 500:
	while a < 334:
		check = (a ** 2) + (b ** 2)
		for i in c:
			if check == i:
				if a + b + math.sqrt(i) == 1000:
					print "Walloper Davis it's " + str(a) + ", " + str(b) + ", " + str(math.sqrt(i))
					print "The product is " + str(a * b * (math.sqrt(i)))
					break
		a += 1
	b += 1
	a = 1	
	print "Round Over"


