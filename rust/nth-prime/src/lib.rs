use std::collections::BTreeSet;

pub fn nth(n: u32) -> u32 {
    if n == 0 {
        return 2
    }

    let un: usize = n as usize;
    let mut primes: BTreeSet<u32> = BTreeSet::new();
    primes.insert(2);
    primes.insert(3);
    let mut next: u32 = 3;

    while primes.len() <= un {
        if is_prime(&primes, next) {
            primes.insert(next);
        }
        next += 2;
    }

    *primes.iter().next_back().expect("No prime found")
}

fn is_prime(known_primes: &BTreeSet<u32>, n: u32) -> bool {
    if n % 2 == 0 {
        return false
    }

    for prime in known_primes.iter() {
        if n % prime == 0 {
            return false;
        }
    }

    let until: u32 = (n as f64).sqrt() as u32;
    let mut num: u32 = *last(&known_primes) + 2;

    while num <= until {
        if n % num == 0 {
            return false
        }
        num += 2
    }

    return true
}

fn last<T>(set: &BTreeSet<T>) -> &T {
    set.iter().next_back().expect("No element found")
}