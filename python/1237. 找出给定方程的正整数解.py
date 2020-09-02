from typing import List
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for i in range(z+1):
            for j in range(z+1):
                if customfunction.f(i,j) == z:
                    res.append((i,j))
        return res