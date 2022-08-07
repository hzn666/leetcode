import sys

for line in sys.stdin:
    if int(line) == 0:
        break

    n = int(line)
    res = 0
    while n >= 3:
        res += n // 3
        n = n // 3 + n % 3
    if n == 2:
        res += 1
    print(res)
