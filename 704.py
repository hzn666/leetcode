# 寻找左侧边界
# 大于等于target的最小下标
def bsl(nums, target):
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


# 寻找右边界
# 小于等于target的最大下标
def bsr(nums, target):
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


# def bsl(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#
#         if nums[mid] == target:
#             right = mid - 1
#         elif nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#
#     if left == len(nums) or nums[left] != target:
#         return -1
#     return left


# 寻找右侧边界
# def bsr(nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#
#         if nums[mid] == target:
#             left = mid + 1
#         elif nums[mid] < target:
#             left = mid + 1
#         elif nums[mid] > target:
#             right = mid - 1
#
#     if right < 0 or nums[right] != target:
#         return -1
#
#     return right


a = [2, 3, 5, 7]
b = 5

print(bsl(a, b))
print(bsr(a, b))
