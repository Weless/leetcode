from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ant = max(nums)
        d_set = set(range(ant))- set(nums)
        return ant+1 if not d_set else d_set.pop()