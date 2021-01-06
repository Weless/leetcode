from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        ans = float("-inf")
        ok = False
        while i<len(nums):
            j = i+1
            while j < len(nums):
                tmp = nums[i] + nums[j]
                if tmp < k:
                    ok = True
                    ans = max(ans,tmp)
                j+=1
            i+=1
        if not ok:
            return -1
        return ans
