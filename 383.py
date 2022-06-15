import collections


def canConstruct(ransomNote: str, magazine: str) -> bool:
    a = collections.Counter(ransomNote)
    b = collections.Counter(magazine)

    for c in ransomNote:
        if a[c] > b[c]:
            return False
    return True