from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for i in arr:
            d[i]+=1
        ans = []
        for k,v in d.items():
            if k == v:
                ans.append(k)
        return max(ans) if ans else -1
