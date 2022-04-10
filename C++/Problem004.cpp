#include <iostream>
#include <string>
#include <cmath>


bool isPalindrome(int num) {
	std::string numStr {std::to_string(num)};
	int len {numStr.length()};

	for (int i {0}; i < len / 2; i++) {
		if (numStr[i] != numStr[len - i - 1])	return false;
	}

	return true;
}


int main() {
	size_t d {3};

	for(int i = pow(pow(10, d) - 1, 2); i >= pow(10, 2 * (d - 1)); i--) {
		if(isPalindrome(i)) {
			for(int j = pow(10, d) - 1; j >= pow(10, d - 1); j--) {
				if((i / j) * j == i && pow(10, d - 1) <= (i / j) && (i / j) <= pow(10, d) - 1) {
					std::cout << i << std::endl;
					return 0;
				}
			}
		}
	}

	return 0;
}