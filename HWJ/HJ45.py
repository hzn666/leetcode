from collections import defaultdict

n = int(input())

for _ in range(n):
    string = input()

    count = defaultdict(int)

    for c in string:
        count[c] += 1

    res = 0
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    for i in range(26, 0, -1):
        if count:
            x = count.pop(0)[1]
            res += i * x
        else:
            break
    print(res)
