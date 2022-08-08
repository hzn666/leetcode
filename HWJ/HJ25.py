I = list(map(int, input().split()))[1:]
R = list(map(int, input().split()))[1:]
R = list(set(R))
R.sort()

res = []

for r in range(len(R)):
    result = []
    for i in range(len(I)):
        if str(R[r]) in str(I[i]):
            result.extend([i, I[i]])
    if result:
        res.append(R[r])
        res.append(len(result) // 2)
        res.extend(result)
_ = [len(res)]
_.extend(res)
for i in _:
    print(i, end=" ")
