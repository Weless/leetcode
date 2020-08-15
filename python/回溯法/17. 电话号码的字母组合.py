from typing import List


class Solution:
    def letterCombinations(self, digits):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(path, next_digits):
            if len(next_digits) == 0:
                output.append(path)
                return
            for letter in phone[next_digits[0]]:
                backtrack(path + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output
s = Solution()
digits = "23"
print(s.letterCombinations(digits))
