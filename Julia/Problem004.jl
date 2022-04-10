function isPalindrome(n)
	return cmp(string(n), reverse(string(n))) == 0
end

# Parameters:
D = 3
###############

for i ∈ (10^D - 1)^2 : -1 : (10^(2*D - 2))
	if isPalindrome(i)
		for j ∈ (10^D - 1) : -1 : (10^(D - 1))
			if i % j == 0
				if (10^(D - 1)) <= i / j && i / j <= (10^D - 1)
					println(i)
					return
				end
			end
		end
	end
end