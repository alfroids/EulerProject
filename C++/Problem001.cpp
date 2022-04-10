#include <iostream>


int main(int argc, char const *argv[]) {
	int sum {0};
	int max {1000};

	for (size_t i = 1; i < max; i++) {
		if (i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
	}

	std::cout << sum << std::endl;

	return 0;
}
