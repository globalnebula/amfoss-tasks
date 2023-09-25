use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..=f64::sqrt(num as f64) as u32 {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn find_primes_up_to_n(n: u32) -> Vec<u32> {
    let mut primes = Vec::new();
    for num in 2..=n {
        if is_prime(num) {
            primes.push(num);
        }
    }
    primes
}

fn main() {
    println!("Enter a number (n):");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read line");

    let n: u32 = input.trim().parse().expect("Invalid input. Please enter a number.");

    let prime_numbers = find_primes_up_to_n(n);

    println!("Prime numbers up to {}: {:?}", n, prime_numbers);
}
