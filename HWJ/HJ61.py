def apple(m, n):
    if m < 0 or n < 0:
        return 0
    elif m == 1 or n == 1:
        return 1
    else:
        return apple(m, n - 1) + apple(m - n, n)


m, n = list(map(int, input().split()))
print(apple(m, n))
