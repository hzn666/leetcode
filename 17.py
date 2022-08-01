class Solution:
    def __init__(self):
        self.res = []
        self.s = ""
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        if not digits:
            return []

        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits, index):
        if index == len(digits):
            self.res.append(self.s)
            return

        letters = self.letter_map[digits[index]]

        for letter in letters:
            self.s += letter
            self.backtrack(digits, index + 1)
            self.s = self.s[:-1]