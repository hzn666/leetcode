sentence = input()

res = ""

for c in sentence:
    if not c.isalpha():
        res += " "
    else:
        res += c

res = res.split()
for i in res[::-1]:
    print(i, end=" ")
