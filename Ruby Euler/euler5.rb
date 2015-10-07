#Andrew Smith
#Feb 22 2015
num = 20
one_twenty = 20
while one_twenty > 0
	if num % one_twenty == 0
		one_twenty -= 1
		puts  one_twenty if one_twenty < 15
	else 
		num += 20
		one_twenty = 20
	end
end
	
puts "The number is: " + num.to_s	
