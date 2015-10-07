#Andrew Smith
#April 29 2013
num_prime = 2
num_count = 4
import time;
start_time = time.time()
def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

while num_prime != 10001:
	num_count += 1
	if is_prime(num_count) == True:
		num_prime += 1
print "Pong!"
print "Finished in " + str(time.time() - start_time) + " seconds!"
print "Prime is: " + str(num_count)
