n = int(input())
res = 0
for i in range(1, n + 1):
    if '7' in str(i):
        res += 1
    elif i % 7 == 0:
        res += 1
print(res)
