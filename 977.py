from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    new_nums = [0] * len(nums)
    pos = len(nums) - 1

    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            new_nums[pos] = nums[left] * nums[left]
            left += 1
        else:
            new_nums[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return new_nums