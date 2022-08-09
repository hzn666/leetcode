alt = [2, 3, 2, 4]

n = int(input())

if n < 3:
    print(-1)
if n >= 3:
    print(alt[(n - 3) % 4])
