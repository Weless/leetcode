from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
        def dfs(path,choice):
            if len(choice) == 0:
                res.append(path)
            for i in range(len(choice)):
                path+=choice[i]
                dfs(path,choice[:i]+choice[i+1:])
                path=path[:-1]
        res = []
        dfs('',S)
        return res
s = Solution()
S = "qwe"
print(s.permutation(S))