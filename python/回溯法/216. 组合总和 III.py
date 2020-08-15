from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(path,k,target,start):
            if k == 0:
                if target == 0:
                    res.append(path[:])
                    return
                return
            for i in range(start,10):
                path.append(i)
                dfs(path,k-1,target-i,i+1)
                path.pop()
        res = []
        dfs([],k,n,1)
        return res

s = Solution()
k = 3
n = 9
print(s.combinationSum3(k,n))