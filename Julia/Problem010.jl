# Parameters:
max = 2000000
################

primes = [2]
i = 3

while true
	for p ∈ primes
		if p^2 > i
			append!(primes, i)
			break
		elseif i % p == 0
			break
		end
	end

	global i += 2

	if i > max
		break
	end
end

println(sum(primes))