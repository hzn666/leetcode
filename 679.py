from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        target = 24
        epsilon = 1e-6

        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - target) < epsilon
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = []
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == 0:
                                newNums.append(x+y)
                            if k == 1:
                                newNums.append(x*y)
                            if k == 2:
                                newNums.append(x-y)
                            if k == 3:
                                if abs(y) < epsilon:
                                    continue
                                newNums.append(x/y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False
        return solve(cards)

