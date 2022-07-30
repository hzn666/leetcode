class Solution:
    def search(self, nums, target):
        def searchl(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(nums) or nums[left] != target:
                return -1

            return left

        def searchr(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    left = mid + 1

            if right < 0 or nums[right] != target:
                return -1

            return right

        if not nums:
            return 0

        left = searchl(nums, target)
        right = searchr(nums, target)

        if left == -1 and right == -1:
            return 0
        return right - left + 1
