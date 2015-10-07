total = 0
x = 3
while x < 1000: 
	
	if x % 3 == 0:
		total = total + x
	elif x % 5 == 0:
		total = total + x
	x += 1

	
x = 0
print total
