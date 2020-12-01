from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        import itertools
        count = 0
        for i in itertools.count(1,1):
            if i not in arr:
                count+=1
                if count == k:
                    return i
