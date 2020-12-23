from typing import List
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        res = 5000
        n = 0
        for i in arr:
            if i > res:
                return n
            else:
                res -= i
                n+=1
        return n