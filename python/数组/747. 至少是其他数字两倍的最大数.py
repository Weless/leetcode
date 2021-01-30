from typing import List
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        t = sorted(nums,reverse=True)
        if t[0] >= 2 * t[1]:
            return nums.index(t[0])
        return -1
