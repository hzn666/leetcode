from collections import defaultdict

string = input()
dic = defaultdict(int)

for i in string:
    dic[i] += 1

min_ = min(dic.values())
res = ""

for i in string:
    if dic[i] != min_:
        res += i

print(res)
