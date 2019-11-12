from typing import List
from typing import Dict
from typing import Tuple
from typing import Deque
from collections import deque

days: Dict[int, Tuple[str, str]] = {
    1: ("first", "and a Partridge in a Pear Tree"),
    2: ("second", "two Turtle Doves"),
    3: ("third", "three French Hens"),
    4: ("fourth", "four Calling Birds"),
    5: ("fifth", "five Gold Rings"),
    6: ("sixth", "six Geese-a-Laying"),
    7: ("seventh", "seven Swans-a-Swimming"),
    8: ("eighth", "eight Maids-a-Milking"),
    9: ("ninth", "nine Ladies Dancing"),
    10: ("tenth", "ten Lords-a-Leaping"),
    11: ("eleventh", "eleven Pipers Piping"),
    12: ("twelfth", "twelve Drummers Drumming")
}


def recite(start_verse, end_verse) -> List[str]:
    return recursive_verses(start_verse, end_verse, [])


template = "On the {} day of Christmas my true love gave to me: {}."


def recursive_verses(current: int, end: int, verses: List[str]) -> List[str]:
    if current > end:
        return verses

    dynamic_part: Deque[str] = deque()
    for v in days:
        if v <= current:
            (_, content) = days[v]
            dynamic_part.appendleft(content)
        else:
            break

    verse = ", ".join(dynamic_part)
    if current == 1:
        verse = verse.replace("and ", "")

    (order, _) = days[current]
    output = template.format(order, verse)
    verses.append(output)

    return recursive_verses(current + 1, end, verses)
