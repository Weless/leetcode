from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        t = 0
        for i in range(len(nums)-1):
            if i == 0:
                if nums[i] > nums[i+1]:
                    nums[i] = nums[i+1]
                    t+=1
            elif nums[i] > nums[i+1] and nums[i-1] <= nums[i+1]:
                t+=1
        return t == 1

s = Solution()
nums = [-1,4,2,3]
print(s.checkPossibility(nums))