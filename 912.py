class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, l, r):
        if l >= r:
            return

        m = (l + r) // 2
        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m + 1, r)

        tmp = nums[l:r + 1]
        i, j = 0, m - l + 1

        for k in range(l, r + 1):
            if i == m - l + 1:
                nums[k] = tmp[j]
                j += 1
            elif j == r - l + 1:
                nums[k] = tmp[i]
                i += 1
            elif tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i += 1
            elif tmp[j] < tmp[i]:
                nums[k] = tmp[j]
                j += 1
