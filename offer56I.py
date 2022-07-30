class Solution:
    def singleNumbers(self, nums):
        x, y, n, m = 0, 0, 0, 1

        for num in nums:
            n ^= num

        while n & m == 0:
            m <<= 1

        for num in nums:
            if num & m == 0:
                x ^= num
            else:
                y ^= num

        return x, y
