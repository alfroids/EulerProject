# Parameters:
maxVal = 1000
###############

sumDiv = 0

for i=1:(maxVal - 1)
	if i % 3 == 0 || i % 5 == 0
		global sumDiv += i
	end
end

println(sumDiv)