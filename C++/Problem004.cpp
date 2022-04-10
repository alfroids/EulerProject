#include <iostream>
#include <string>


// Method that returns true if a given number is a palindrome
bool isPalindrome(int num) {
	std::string numStr {std::to_string(num)};
	int len {numStr.length()};

	for (int i {0}; i < len / 2; i++) {
		if (numStr[i] != numStr[len - i - 1])	return false;
	}

	return true;
}


int main() {
	for(int i = 999 * 999; i >= 100 * 100; i--) {
		if(isPalindrome(i)) {
			for(int j = 999; j >= 100; j--) {
				if((i / j) * j == i && 100 <= (i / j) && (i / j) <= 999) {
					std::cout << i << std::endl;
					return 0;
				}
			}
		}
	}

	return 0;
}