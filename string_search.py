def search_substring(s1: str, s2: str) -> int:
    if s1 in s2:
        return s2.index(s1)
    else:
        return -1