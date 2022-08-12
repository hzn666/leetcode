def dfs(nums):
    if not nums:
        return False
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6

    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i != j:
                newNums = []
                for k, c in enumerate(nums):
                    if k != i and k != j:
                        newNums.append(c)
                for k in range(4):
                    if k < 2 and i > j:
                        continue
                    if k == 0:
                        newNums.append(a + b)
                    if k == 1:
                        newNums.append(a * b)
                    if k == 2:
                        newNums.append(a - b)
                    if k == 3:
                        if abs(b) < 1e-6:
                            continue
                        newNums.append(a / b)
                    if dfs(newNums):
                        return True
                    newNums.pop()
    return False


while True:
    try:
        lst = [int(x) for x in input().split()]

        if dfs(lst):
            print("true")
        else:
            print("false")
    except:
        break
