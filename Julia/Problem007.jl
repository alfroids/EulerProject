# Parameters:
pos = 10001
################

primes = [2]
i = 3

while length(primes) < pos
	for p ∈ primes
		if p^2 > i
			append!(primes, i)
			break
		elseif i % p == 0
			break
		end
	end
	
	global i += 2
end

println(primes[end])