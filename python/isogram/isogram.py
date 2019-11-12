def is_isogram(string: str):
    normalized = string.replace("-", "").replace(" ", "").lower()
    return len(normalized) == set(normalized).__len__()
