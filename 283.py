from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # cur存储为0的索引
    cur = 0

    for item in nums:
        if item != 0:
            nums[cur] = item
            cur += 1

    while cur < len(nums):
        nums[cur] = 0
        cur += 1
