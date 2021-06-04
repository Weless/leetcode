from typing import List
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        cnt = 0
        for i,v in c.items():
            if v == 1:
                cnt+=i
        return cnt
