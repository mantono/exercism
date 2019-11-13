from typing import Dict
from typing import List
import re

match_on = re.compile("\\w+('\\w+)?")
delimiter = re.compile("[\\s_,]+")


def count_words(sentence: str) -> Dict[str, int]:
    words: List[str] = delimiter.split(sentence)
    words: List[str] = [
        re.search(match_on, w).group(0).lower()
        for w in words if len(w) > 0
    ]
    return dict((k, words.count(k)) for k in words)
