n, k = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()

for i in num[:k]:
    print(i, end=" ")
