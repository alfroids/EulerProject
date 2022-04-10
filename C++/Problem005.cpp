#include <iostream>
#include <vector>


std::vector<int> primeFactors(int num) {
	std::vector<int> factors;
	int p {2};

	while (p * p <= num) {
		if (num % p == 0) {
			factors.push_back(p);
			num /= p;
		} else {
			p++;
		}
	}

	if (num > 1)
		factors.push_back(num);

	return factors;
}


int main() {
	size_t num {1};
	size_t max {20};

	for(size_t i = 1; i <= max; i++) {
		size_t temp {num};
		for(auto j : primeFactors(i)) {
			if(temp % j != 0)	num *= j;
			else				temp /= j;
		}
	}

	std::cout << num << std::endl;

	return 0;
}