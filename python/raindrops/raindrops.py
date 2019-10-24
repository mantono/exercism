def convert(number: int) -> str:
    factors = []
    if number % 3 == 0:
        factors.append("Pling")
    if number % 5 == 0:
        factors.append("Plang")
    if number % 7 == 0:
        factors.append("Plong")
    if len(factors) == 0:
        factors.append(str(number))
    return "".join(factors)
