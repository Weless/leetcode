from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set()
        for i,j in ranges:
            for v in range(i,j+1):
                s.add(v)

        for i in range(left,right+1):
            if i not in s:
               return False
        return True

s = 
