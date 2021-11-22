# 回文数

# 我的方法
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         rev = 0
#         if x >= 0:
#             num = x
#             while x != 0:
#                 digit = x % 10
#                 if x < 0 and digit > 0:
#                     digit -= 10
#                 x = (x - digit) // 10
#                 rev = rev * 10 + digit
#
#             if rev == num:
#                 return True
#         return False

# 官方题解
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        print(x, rev)
        return x == rev or x == rev // 10


s = Solution()
print(s.isPalindrome(11))
