n = int(input())

list1 = [[0] * i for i in range(1, n + 1)]

a = 0

for i in range(n):
    for j in range(i + 1):
        a += 1
        list1[i][j] = a

list2 = []
she = []

for i in range(n):
    for line in list1:
        if line:
            list2.append(line.pop(-1))
    she.append(" ".join(map(str, list2)))
    list2 = []

for i in she:
    print(i)
