string = input()

dic = {}

for c in string:
    if c not in dic:
        dic[c] = True
    else:
        dic[c] = False

for k, v in dic.items():
    if v:
        print(k)
        break
else:
    print(-1)
