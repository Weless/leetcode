from typing import List

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if Amax - Amin <= 2 * K:
            return 0
        else:
            return Amax-Amin-4


s =Solution()
A = [0,10]
K = 2
print(s.smallestRangeI(A,K))