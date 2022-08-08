a = input()

res = []

for i in a:
    res.append(int(ord(i)))

res.sort()

for i in res:
    print(chr(i), end="")
