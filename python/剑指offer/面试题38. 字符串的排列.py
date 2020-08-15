from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(path,s):
            if len(s) == 0:
                res.append(path)
                return
            for i in range(len(s)):
                if i > 0 and s[i] == s[i-1]: continue
                dfs(path+s[i],s[:i]+s[i+1:])
        res = []
        s = sorted(s)
        dfs('',s)
        return res

s = Solution()
test = "aab"
print(s.permutation(test))