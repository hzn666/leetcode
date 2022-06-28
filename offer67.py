def strToInt(str: str) -> int:
    res = 0
    i = 0
    sign = 1
    length = len(str)

    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    bndry = 2 ** 31 // 10

    if not str:
        return 0

    while str[i] == " ":
        i += 1
        if i == length:
            return 0

    if str[i] in "+-":
        if str[i] == "-":
            sign = -1
        i += 1

    for j in range(i, length):
        if not "0" <= str[j] <= "9":
            break
        if res > bndry or res == bndry and str[j] > "7":
            return int_max if sign == 1 else int_min
        res = 10 * res + ord(str[j]) - ord("0")

    return sign * res

print(strToInt("4193 with words"))