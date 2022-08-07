if __name__ == '__main__':
    num = int(input())
    res = 0
    while num:
        if num % 2:
            res += 1
        num //= 2
    print(res)
