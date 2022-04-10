# Parameters:
sum_ = 1000
################

for a in 1 : sum_ - 2
	for b in 1 : sum_ - a - 1
		c = sum_ - a - b
		if a^2 + b^2 == c^2
			println(a * b * c)
			return
		end
	end
end