from typing import List


def distance(strand_a: List[object], strand_b: List[object]) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Inputs have different length")
    length: int = len(strand_a)
    matches: int = 0
    for s0, s1 in zip(strand_a, strand_b):
        if s0 == s1:
            matches += 1

    return length - matches
