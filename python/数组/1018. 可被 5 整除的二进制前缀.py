from typing import List
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        tmp = 0
        for i in A:
            tmp = (tmp*2+i)%5
            res.append(tmp==0)
        return res