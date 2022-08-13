class Solution:
    def letterCombinations(self, digits):
        res = []
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if not digits:
            return []

        def backtracking(digits, index, s):
            if len(s) == len(digits):
                res.append(s)
                return

            letters = letter_map[digits[index]]

            for letter in letters:
                backtracking(digits, index + 1, s+letter)

        backtracking(digits, 0, "")
        return res
