#include <iostream>
#include <vector>


unsigned long int numDivisors(unsigned long int n) {
	if (n == 0) {
		return 0;
	}

	unsigned long int divisors {}, i {1};

	while (i * i <= n) {
		if (n % i == 0) {
			if (n / i == i)	divisors++;
			else			divisors += 2;
		}

		i++;
	}

	return divisors;
}


int main() {
	// Parameters:
	int minDivs = 500;
	///////////////

	unsigned long int count {1}, triNum {0};

	while (numDivisors(triNum) < minDivs) {
		triNum += count;
		count++;
	}

	std::cout << triNum << std::endl;

	return 0;
}