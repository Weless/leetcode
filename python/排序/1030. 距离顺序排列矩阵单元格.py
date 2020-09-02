from typing import List
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R):
            for j in range(C):
                res.append((i,j))
        return sorted(res,key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))

s = Solution()
R = 1
C = 2
r0 = 0
c0 = 0
print(s.allCellsDistOrder(R,C,r0,c0))