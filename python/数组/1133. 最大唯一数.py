from typing import List
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for i in A:
            d[i]+=1
        max_num = float('-inf')
        ok = False
        for k,v in d.items():
            if v > 1 :
                continue
            max_num = max(max_num,k)
            ok = True
        if not ok:
            return -1
        return max_num