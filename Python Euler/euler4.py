import time
def palindrome():
	hank = True
	num1 = 100
	num2 = 100
	answer = 0
	possible_answers = {}
	a = b = 0
	while hank == True:
		answer = num1 * num2
		#flip_answer = str(answer)
		#flip_answer = flip_answer[::-1]
		#flip_answer = int(answer)
		#iprint flip_answer
		#print answer
		if answer == int(str(answer)[::-1]):
			mult = str(num1) + " X " + str(num2)
			possible_answers[mult] = answer
			print mult + " Equals " + str(answer)
		
		num2 += 1
		if num2 == 1000:
			num2 = 100
			num1 += 1
			if num1 == 1000:
				print "DONE"
				time.sleep(1)
				hank = False
				
				
	#print possible_answers
	for i in possible_answers:
		a = possible_answers[i]		
		
		if a > b:
			b = a
	the_palindrome = b
	for i in possible_answers:
		if possible_answers[i] == the_palindrome:
			print "HooRay!!" 
			print i + " equals " + str(the_palindrome)
	

palindrome()
	
