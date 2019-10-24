from typing import List


def latest(scores: List[int]) -> int:
    return scores[len(scores)-1]


def personal_best(scores: List[int]) -> int:
    scores.sort()
    return latest(scores)


def personal_top_three(scores: List[int]) -> List[int]:
    scores.sort()
    scores.reverse()
    return scores[0:3]
