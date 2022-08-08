I = []
for i in range(26):
    I.append(chr(ord('a') + i))

key = input()
s = input()

new = []
for i in key:
    if i not in new:
        new.append(i)

for i in I:
    if i not in new:
        new.append(i)

m = dict(zip(I, new))

res = []

for i in s:
    res.append(m[i])
print("".join(res))
