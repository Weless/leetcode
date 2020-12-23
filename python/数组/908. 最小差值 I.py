from typing import List
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        _min,_max = min(A),max(A)
        if _max -_min <= 2 * K:
            return 0
        else:
            return _max - _min - 2* K