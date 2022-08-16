def merge_sort(nums, l, r):
    if l >= r:
        return

    m = (l + r) // 2
    merge_sort(nums, l, m)
    merge_sort(nums, m + 1, r)

    tmp = nums[l:r + 1]
    # i,j分别为tmp的左右子数组的首元素
    i, j = 0, m - l + 1

    for k in range(l, r + 1):
        # 左子数组已合并完，因此添加右子数组
        if i == m - l + 1:
            nums[k] = tmp[j]
            j += 1
        # 右子数组已合并完，因此添加左子数组
        # 左子数组的小于右子数组，添加左子数组
        elif j == r - l + 1 or tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
        # 右子数组的小于左子数组，添加右子数组
        else:
            nums[k] = tmp[j]
            j += 1


nums = [3, 4, 1, 5, 2, 1]
merge_sort(nums, 0, len(nums) - 1)
print(nums)
