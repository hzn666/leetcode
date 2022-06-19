def repeatedSubstringPattern(s: str) -> bool:
    for i in range(len(s) - 1):
        temp = s[i + 1:] + s[:i + 1]
        if temp == s:
            return True
    return False


s = "abab"
repeatedSubstringPattern(s)
