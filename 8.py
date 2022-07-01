def myAtoi(s: str) -> int:
    res = 0
    i = 0
    sign = 1
    length = len(s)

    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    bndry = 2 ** 31 // 10

    if not s:
        return 0

    while s[i] == " ":
        i += 1
        if i == length:
            return 0

    if s[i] in "+-":
        if s[i] == "-":
            sign = -1
        i += 1

    for j in range(i, length):
        if not "0" <= s[j] <= "9":
            break
        if res > bndry or res == bndry and s[j] > "7":
            return int_max if sign == 1 else int_min
        res = 10 * res + ord(s[j]) - ord("0")

    return sign * res