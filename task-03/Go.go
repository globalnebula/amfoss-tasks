package main

import (
    "fmt"
    "math"
)

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    if num <= 3 {
        return true
    }
    if num%2 == 0 || num%3 == 0 {
        return false
    }
    for i := 5; i*i <= num; i += 6 {
        if num%i == 0 || num%(i+2) == 0 {
            return false
        }
    }
    return true
}

func main() {
    var n int
    fmt.Print("Enter a number (n): ")
    fmt.Scan(&n)

    fmt.Printf("Prime numbers up to %d are:\n", n)
    for i := 2; i <= n; i++ {
        if isPrime(i) {
            fmt.Println(i)
        }
    }
}
