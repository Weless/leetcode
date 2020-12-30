from typing import List
class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i,v in enumerate(A):
            if i == v:
                return v
        return -1