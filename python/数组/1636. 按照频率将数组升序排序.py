from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in nums:
            
