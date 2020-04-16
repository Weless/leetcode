from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        if len(nums) == 1:
            return nums.pop()
        aMax = -1000000
        # maxi,maxj = 0,0
        i,j = 0,len(nums)-1
        while i <=j:
            temp = sum(nums[i:j+1])
            if temp > aMax:
                aMax = temp
                # maxi,maxj = i,j
            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
        return aMax
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-2,-1]
print(s.maxSubArray(nums2))