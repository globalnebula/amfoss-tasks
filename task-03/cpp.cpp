#include <iostream>
#include <vector>
#include <cmath>

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(num); ++i) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

std::vector<int> findPrimesUpToN(int n) {
    std::vector<int> primes;
    for (int num = 2; num <= n; ++num) {
        if (isPrime(num)) {
            primes.push_back(num);
        }
    }
    return primes;
}

int main() {
    std::cout << "Enter a number (n): ";
    int n;
    std::cin >> n;

    std::vector<int> primeNumbers = findPrimesUpToN(n);

    std::cout << "Prime numbers up to " << n << ": ";
    for (int prime : primeNumbers) {
        std::cout << prime << " ";
    }
    std::cout << std::endl;

    return 0;
}
