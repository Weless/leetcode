class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        return re.match(p,s).group()
s = Solution()
a = "aa"
b = "a"
print(s.isMatch(a,b))