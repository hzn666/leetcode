from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def searchl(nums: List[int], target: int) -> int:
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

    def searchr(nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if right < 0 or nums[right] != target:
            return -1

        return right

    left = searchl(nums, target)
    right = searchr(nums, target)

    if left == -1 or right == -1:
        return [-1, -1]
    else:
        return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(nums, target))