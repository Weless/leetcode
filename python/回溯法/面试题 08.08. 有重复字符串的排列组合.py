from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:

        def dfs(path,s,l):
            if len(path) == l:
                res.append(''.join(path))
                return
            for i in range(len(s)):
                if i>0 and s[i-1] == s[i]:continue
                path.append(s[i])
                dfs(path,s[:i]+s[i+1:],l)
                path.pop()
        if not S:
            return []
        res = []
        s = sorted(S)
        l = len(s)
        dfs([],s,l)
        return res

s = Solution()
S = "qqe"
print(s.permutation(S))