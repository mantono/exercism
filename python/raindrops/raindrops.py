def convert(number: int) -> str:
    factors = []
    for factor, raindrop in divisors.items():
        if number % factor == 0:
            factors.append(raindrop)
    if len(factors) == 0:
        factors.append(str(number))
    return "".join(factors)


divisors = {
    3: "Pling",
    5: "Plang",
    7: "Plong"
}
