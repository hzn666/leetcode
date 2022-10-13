import random


def quick_sort(nums, l, r):
    if l >= r:
        return
    i = partition(nums, l, r)
    quick_sort(nums, l, i - 1)
    quick_sort(nums, i + 1, r)


def partition(nums, l, r):
    ra = random.randrange(l, r + 1)
    nums[l], nums[ra] = nums[ra], nums[l]
    i, j = l, r
    while i < j:
        while i < j and nums[j] >= nums[l]:
            j -= 1
        while i < j and nums[i] <= nums[l]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[l] = nums[l], nums[i]
    return i
