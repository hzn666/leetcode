def strStr(haystack: str, needle: str) -> int:
    n = len(haystack)
    m = len(needle)

    i = 0
    while i+m <= n:
        flag = True
        for j in range(m):
            if haystack[i+j] != needle[j]:
                flag = False
                break

        if flag:
            return i
        i += 1

    return -1

haystack = "hello"
needle = "ll"
strStr(haystack, needle)
