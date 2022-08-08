n = int(input())
m = list(map(int, input().split()))
x = list(map(int, input().split()))

amount = []
weight = {0, }

for i in range(n):
    for j in range(x[i]):
        amount.append(m[i])

for i in amount:
    for j in list(weight):
        weight.add(i + j)

print(len(weight))
