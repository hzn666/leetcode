height = int(input())

res = height

for _ in range(4):
    height /= 2
    if _ == 4:
        res += height
    else:
        res += height * 2

print(res)
print(height / 2)
