#Andrew Smith
#Apr 29 2015
x = 5
addition = 5
keepTrack = []
def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

while x < 2000000:
	if is_prime(x):
		addition += x
		keepTrack.append(x)
	x += 1
	if x == 500000:
		print "500 Baby!"
	elif x == 100000:
                print "100 Baby!"
	elif x == 1000000:
                print "A Cool One"
	elif x == 2000000:
		print "All Done! Your sum sir: " + str(addition)
