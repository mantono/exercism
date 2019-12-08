pub fn nth(n: u32) -> u32 {
    if n == 0 {
        return 2
    }

    let un: usize = n as usize;
    let mut primes: Vec<u32> = Vec::with_capacity(un/4);
    primes.push(2);
    primes.push(3);

    (2..)
        .filter(|p|
            if is_prime(&primes, p.clone()) {
                primes.push(*p);
                true
            } else {
                false
            }
        )
        .nth(un)
        .unwrap()
}

#[inline]
fn is_prime(known_primes: &Vec<u32>, n: u32) -> bool {
    let limit: u32 = (n as f64).sqrt() as u32;
    let certain_composite: bool = known_primes.iter()
        .take_while(|prime| prime <= &&limit)
        .any(|&prime| n % prime == 0);

    if certain_composite {
        return false
    }

    let start: u32 = *known_primes.last().unwrap_or(&3);
    (start..=limit).step_by(2).all(|prime| n % prime != 0)
}