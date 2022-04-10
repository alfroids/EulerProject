function primeFactors(n)
	factors = zeros(0)
	p = 2

	while p^2 <= n
		if n % p == 0
			append!(factors, p)
			n /= p
		else
			p += 1
		end
	end

	if n > 1
		append!(factors, n)
	end

	return factors
end

# Parameters:
maxNum = 20
################

divNum = 1

for i ∈ 2 : maxNum
	temp = divNum
	for f ∈ primeFactors(i)
		if temp % f == 0
			temp /= f
		else
			global divNum *= f
		end
	end
end

println(Int(divNum))