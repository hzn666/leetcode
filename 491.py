from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(index, path):
            if len(path) >= 2:
                if path[-1] >= path[-2]:
                    res.append(path)
                else:
                    return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                backtracking(i + 1, path + [nums[i]])

        backtracking(0, [])
        return res


if __name__ == '__main__':
    so = Solution()
    print(so.findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]))
