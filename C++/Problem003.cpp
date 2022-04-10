#include <iostream>


int main() {
	size_t num {600851475143};
	int p {2};

	while (p * p < num) {
		if (num % p == 0)	num /= p;
		else 				p++;
	}

	std::cout << num << std::endl;

	return 0;
}