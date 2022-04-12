#include <iostream>


size_t min(size_t a, size_t b) {
	return (a < b) ? a : b;
}


unsigned long long binomialCoeff(size_t n, size_t k)
{
    unsigned long long C[n + 1][k + 1];
    size_t i, j;
 
    for (i = 0; i <= n; i++) {
        for (j = 0; j <= min(i, k); j++) {
            if (j == 0 || j == i)	C[i][j] = 1;
			else					C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }
 
    return C[n][k];
}


int main() {
	// Parameters:
	size_t N {20};
	///////////////

	std::cout << binomialCoeff(2 * N, N) << std::endl;

	return 0;
}