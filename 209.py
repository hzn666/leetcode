from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    result = float("inf")
    sum = 0
    index = 0

    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            result = min(result, i - index + 1)
            sum -= nums[index]
            index += 1

    return 0 if result == float("inf") else result


nums = [2, 3, 1, 2, 4, 3]
target = 7

print(minSubArrayLen(target, nums))
