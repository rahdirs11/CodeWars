def scramble(s1: str, s2: str) -> bool:
    if len(s1) == 0 or len(s2) == 0:
        return False
    for s in set(s2):
        if s2.count(s) > s1.count(s):   return False
    return True
