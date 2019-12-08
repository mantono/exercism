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

#[inline]
fn is_prime(known_primes: &Vec<u32>, n: u32) -> bool {
    if n % 2 == 0 {
        return false
    }

    let limit: u32 = (n as f64).sqrt() as u32;
    let certain_composite: bool = known_primes.iter()
        .take_while(|prime| prime <= &&limit)
        .any(|&prime| n % prime == 0);

    if certain_composite {
        return false
    }

    let mut num: u32 = coerce_to_odd(limit);

    while num <= limit {
        if n % num == 0 {
            return false
        }
        num += 2
    }

    return true
}

fn coerce_to_odd(n: u32) -> u32 {
    if n % 2 == 0 {
        n + 1
    } else {
        n
    }
}