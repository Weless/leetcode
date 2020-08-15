from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(path,start):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start,n+1):
                path.append(i)
                dfs(path,i+1)
                path.pop()
        res = []
        dfs([],1)
        return res
s = Solution()
n = 4
k = 2
print(s.combine(n,k))