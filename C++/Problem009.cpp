#include <iostream>


int main() {
	// Parameters:
	int S {1000};
	///////////////

	for(int a = 1; a <= S - 2; a++) {
		for(int b = 1; b <= S - a - 1; b++) {
			int c = S - a - b;

			if(a * a + b * b == c * c) {
				std::cout << a * b * c << std::endl;
				return 0;
			}
		}
	}

	return 0;
}