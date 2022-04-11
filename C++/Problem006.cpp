#include <iostream>


int main() {
	// Parameters:
	int N {100};
	///////////////

	int sumSqr {0};
	int sqrSum {0};

	for(int i = 1; i <= N; i++) {
		sumSqr += i * i;
		sqrSum += i;
	}
	sqrSum *= sqrSum;

	std::cout << sqrSum - sumSqr << std::endl;

	return 0;
}