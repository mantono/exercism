from typing import Dict
from typing import List
import re

pattern = re.compile("\\w+('\\w+)?")
split = re.compile("[\\s_,]+")

def count_words(sentence: str) -> Dict[str, int]:
    words: List[str] = split.split(sentence)
    words: List[str] = [re.search(pattern, x).group(0).lower() for x in words if len(x) > 0]
    words: Dict[str, int] = dict((k, words.count(k)) for k in words)
    print(words)
    return words
