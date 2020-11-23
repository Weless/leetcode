class Solution:
    def maxScore(self, s: str) -> int:
        cur = ones = 0
        res = -1
        for i, c in enumerate(s):
            if c == '0':
                cur += 1
            else:
                cur -= 1
                ones += 1
            if i < len(s) - 1:
                res = max(res, cur)
        return res + ones