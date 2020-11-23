from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        A = {}
        for x,y in paths:
            if x not in A:
                A[x] = -1
            else:
                A[x] -=1
            if y not in A:
                A[y] = 1
            else:
                A[y] += 1
        for k,v in A.items():
            if v > 0 :
                return k
s = Solution()
paths = [["B","C"],["D","B"],["C","A"]]
print(s.destCity(paths))
