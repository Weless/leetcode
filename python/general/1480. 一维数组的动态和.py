from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for i in range(len(res)):
            j = 0
            while j <= i:
                res[i] += nums[j]
                j+=1
        return res