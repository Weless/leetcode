from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums)

