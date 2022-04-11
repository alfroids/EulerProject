#include <iostream>
#include <vector>


int main() {
	// Parameters:
	int pos {10001};
	///////////////

	std::vector<int> primes {};

	primes.push_back(2);
	int i {3};

	while(primes.size() < pos) {
		for(auto p : primes) {
			if(p * p > i) {
				primes.push_back(i);
				break;
			} else if (i % p == 0) {
				break;
			}
		}

		i += 2;
	}

	std::cout << primes[pos - 1] << std::endl;

	return 0;
}