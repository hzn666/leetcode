import re


def encode(i):
    if re.search(r'[0-9A-Fa-f]', i):
        return hex(int(bin(int(i, 16))[2:].rjust(4, "0")[::-1], 2))[2:].upper()
    else:
        return i


a = list(input().replace(" ", ""))
a[::2] = sorted(a[::2])
a[1::2] = sorted(a[1::2])

res = ""

for i in a:
    res += encode(i)

print(res)
