if __name__ == '__main__':
    string = list(input()[2:])

    res = 0
    i = 0
    dic = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    while string:
        c = string.pop()

        if c in dic:
            res += dic[c] * 16 ** i
        else:
            res += int(c) * 16 ** i
        i += 1

    print(res)
