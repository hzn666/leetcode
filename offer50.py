def firstUniqChar(s):
    res = dict()

    for c in s:
        res[c] = not c in res

    for k, v in res.items():
        if v:
            return k

    return " "


firstUniqChar("leeleodo")