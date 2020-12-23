from typing import List
class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set()
        ans = 0
        for i in arr:
            if i+1 in s:
                ans+=1
            else:
                if i+1 in arr:
                    ans+=1
                    s.add(i+1)
        return ans

