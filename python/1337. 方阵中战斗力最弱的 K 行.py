from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        nums = [(v.count(1),i) for i,v in enumerate(mat)]
        nums.sort()
        res = []
        for _,j in nums:
            if k == 0: break
            res.append(j)
            k-=1
        return res
s = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(s.kWeakestRows(mat,k))