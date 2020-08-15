from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        length = len(s)
        self.dfs(s, length, 0, [], res)
        return res

    def dfs(self, s, length, start, path, res):
        if start == length:
            res.append(path[:])
            return
        for i in range(start, length):
            if not self.checkPalindrome(s, start, i):
                continue
            path.append(s[start:i + 1])
            self.dfs(s, length, i + 1, path, res)
            path.pop()

    def checkPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True
s = Solution()
test = "aab"
print(s.partition("aab"))