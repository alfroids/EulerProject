function getSeqSize(num)
	if get(seqSize, num, -1) != -1
		return get(seqSize, num, -1)
	end

	if num % 2 == 0
		x = getSeqSize(num / 2)
		seqSize[num] = x + 1
	else
		x = getSeqSize(3 * num + 1)
		seqSize[num] = x + 1
	end

	return x + 1
end


# Parameters:
max_ = 1000000
###############

seqSize = Dict{UInt64, UInt64}(1 => 1)
maxSeq = 1
num = 1

for i ∈ 2 : max_
	s = getSeqSize(i)
	if s > maxSeq
		global maxSeq = s
		global num = i
	end
end

println(num)
