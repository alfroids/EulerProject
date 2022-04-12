#include <iostream>
#include <map>


std::map<unsigned long int, unsigned long int> seqSize {{1, 1}};


unsigned long int getSeqSize(unsigned long int n) {
	if (seqSize.find(n) != seqSize.end()) {
		return seqSize[n];
	}

	unsigned long int x {};
	if (n % 2 == 0)	x = getSeqSize(n / 2);
	else			x = getSeqSize(3 * n + 1);

	seqSize[n] = x + 1;
	return x + 1;
}


int main() {
	// Parameters:
	unsigned long int max = 1000000;
	///////////////

	unsigned long int maxSeq {1}, num {1};

	for (unsigned long int i = 2; i <= max; i++) {
		unsigned long int seq {getSeqSize(i)};
		if (seq > maxSeq) {
			maxSeq = seq;
			num = i;
		}
	}

	std::cout << num << std::endl;

	return 0;
}