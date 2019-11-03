pub fn raindrops(n: u32) -> String {
    let mut drops: Vec<String> = Vec::with_capacity(3);
    if n % 3 == 0 {
        drops.push("Pling".to_string())
    }
    if n % 5 == 0 {
        drops.push("Plang".to_string())
    }
    if n % 7 == 0 {
        drops.push("Plong".to_string())
    }
    if drops.is_empty() {
        drops.push(n.to_string())
    }
    drops.join("")
}