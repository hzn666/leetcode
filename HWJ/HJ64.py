n = int(input())
order = input()

lst = [i for i in range(1, n + 1)]

f = 1
p = 1

if n < 5:
    for i in order:
        if i == 'U':
            if p == 1:
                p = n
            else:
                p -= 1
        if i == 'D':
            if p == n:
                p = 1
            else:
                p += 1
else:
    for i in order:
        if i == 'U':
            if f == 1 and p == 1:
                f = n - 3
                p = 4
            elif p == 1:
                f -= 1
            else:
                p -= 1
        if i == 'D':
            if f == n - 3 and p == 4:
                f = 1
                p = 1
            elif p == 4:
                f += 1
            else:
                p += 1
for i in lst[f - 1:f + 3]:
    print(i, end=" ")
print()
print(f + p - 1)
