# Parameters:
num = 600851475143
################

p = 2

while p^2 < num
	if num % p == 0
		global num /= p
	else
		global p += 1
	end
end

println(Int(num))

