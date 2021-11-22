from typing import List


# 两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
