from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)

    result = []
    n = len(nums)

    for i in range(n):
        left = i + 1
        right = n - 1

        # i剪枝，如果排序后的第一个数大于0了，就不可能三个数和为0
        if nums[i] > 0:
            break
        # i去重
        if i >= 1 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # left去重
                while left != right and nums[left] == nums[left + 1]:
                    left += 1
                # right去重
                while left != right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
