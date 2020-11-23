from typing import List
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        from collections import  defaultdict
        d = defaultdict(list)
        for i in range(R):
            for j in range(C):
                d[abs(r0-i)+abs(c0-j)].append([i,j])
        res = []
        for i in sorted(d):
            res.extend(d[i])
        return res
s = Solution()
R = 2
C = 3
r0 = 1
c0 = 2
print(s.allCellsDistOrder(R,C,r0,c0))