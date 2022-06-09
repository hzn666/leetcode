import bisect
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.recs = rects
        self.arr = [0]
        for x1, y1, x2, y2 in rects:
            self.arr.append(self.arr[-1] + (x2 - x1 + 1) * (y2 - y1 + 1))

    def searchl(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left == len(nums) or nums[left] != target:
            return -1

        return left

    def pick(self) -> List[int]:
        w = random.randint(1, self.arr[-1])
        idx = bisect.bisect_left(self.arr, w) - 1
        x1, y1, x2, y2 = self.recs[idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]
