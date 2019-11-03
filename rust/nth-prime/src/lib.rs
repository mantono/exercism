pub fn nth(n: u32) -> u32 {
    if n == 0 {
        return 2
    }

    let un: usize = n as usize;
    let mut primes: Vec<u32> = Vec::with_capacity(un/4);
    primes.push(2);
    primes.push(3);
    let mut next: u32 = 3;

    while primes.len() <= un {
        if is_prime(&primes, next) {
            primes.push(next);
        }
        next += 2;
    }

    *primes.last().expect("No prime found")
}

fn is_prime(known_primes: &Vec<u32>, n: u32) -> bool {
    if n % 2 == 0 {
        return false
    }

    for prime in known_primes.iter() {
        if n % prime == 0 {
            return false;
        }
    }

    let until: u32 = (n as f64).sqrt() as u32;
    let mut num: u32 = known_primes.last().expect("No element found") + 2;

    while num <= until {
        if n % num == 0 {
            return false
        }
        num += 2
    }

    return true
}