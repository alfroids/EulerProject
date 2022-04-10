# Parameters:
maxVal = 4000000
################

f0, f1 = 1, 2
sumEvn = 2

while f1 < maxVal
	f = f0 + f1
	global f0 = f1
	global f1 = f
	if f % 2 == 0
		global sumEvn += f
	end
end

println(sumEvn)