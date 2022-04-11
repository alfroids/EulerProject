#include <iostream>
#include <vector>


int main() {
	// Parameters:
	long int max_ {2000000};
	///////////////

	long long int sum_ {2};

	std::vector<int> primes {};

	primes.push_back(2);
	int i {3};

	while(i < max_) {
		for(auto p : primes) {
			if(p * p > i) {
				primes.push_back(i);
				sum_ += i;
				break;
			} else if (i % p == 0) {
				break;
			}
		}

		i += 2;
	}

	std::cout << sum_ << std::endl;

	return 0;
}