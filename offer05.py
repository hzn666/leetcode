def replaceSpace(s: str) -> str:
    counter = s.count(" ")

    res = list(s)
    res.extend([' '] * counter * 2)

    left = len(s) - 1
    right = len(res) - 1

    while left >= 0:
        if res[left] != " ":
            res[right] = res[left]
            right -= 1
        else:
            res[right - 2:right + 1] = "%20"
            right -= 3
        left -= 1

    return "".join(res)
