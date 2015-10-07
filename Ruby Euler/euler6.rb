tnum = 0
nnum = 0

tnum2 = 0
nnum2 = 0
finalnum = 0

while nnum < 101 
	tnum += nnum**2
	nnum += 1
	end
while nnum2 < 101
	tnum2 += nnum2
	nnum2 += 1
	if nnum2 == 101
		tnum2 = tnum2 ** 2
	end
end
finalnum = tnum2 - tnum
puts "The answer is " + finalnum.to_s
