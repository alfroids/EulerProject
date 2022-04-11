function getNumDivisors(num)
	if num == 0
		return 0
	end

	divisors = zeros(0)
	i = 1

	while i * i <= num
		if num % i == 0
			if num / i == i
				append!(divisors, i)
			else
				append!(divisors, i)
				append!(divisors, Int(num / i))
			end
		end
		i += 1
	end

	return length(divisors)
end


# Parameters:
minDivs = 500
###############

count = 1
triNum = 0

while getNumDivisors(triNum) <= minDivs
	global triNum += count
	global count += 1
end

println(triNum)