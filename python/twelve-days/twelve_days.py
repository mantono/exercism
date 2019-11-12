from typing import List
from typing import Dict

days: Dict[int, (str, str)] = {
    1: ("first", "and a Partridge in a Pear Tree."),
    2: ("second", "two Turtle Doves"),
    3: ("third", "three French Hens"),
    4: ("fourth", "four Calling Birds"),
    5: ("fifth", "five Gold Rings"),
    6: ("sixth", "six Geese-a-Laying"),
    7: ("seventh", "seven Swans-a-Swimming"),
    8: ("eight", "eight Maids-a-Milking"),
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

    (order, _) = days[current]
    for v in days:
        if current <= v <= end:
            print(days[v]) # <-- Work in progress
    verse = "" # <-- Work in progress
    if current == 1:
        verse = verse.replace("and ", "")
    output = template.format(order, verse)
    verses.append(output)

    return recursive_verses(current + 1, end, verses)
