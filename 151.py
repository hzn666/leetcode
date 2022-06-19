def reverseWords(s: str) -> str:
    def trim_spaces(s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1

        tmp = []
        while left <= right:
            if s[left] != " ":
                tmp.append(s[left])
            elif tmp[-1] != " ":
                tmp.append(s[left])
            left += 1
        return tmp

    def reverse_string(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    def reverse_each_word(nums):
        start = 0
        end = 0

        n = len(nums)

        while start < n:
            while end < n and nums[end] != " ":
                end += 1
            reverse_string(nums, start, end - 1)
            start = end + 1
            end += 1
        return None

    l = trim_spaces(s)
    reverse_string(l, 0, len(l) - 1)
    reverse_each_word(l)
    return "".join(l)


a = "a good   example"
print(reverseWords(a))
