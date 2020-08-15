from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        # dp[i] 代表以元素nums[i] 为结尾的连续子数组最大和
        for i in range(1,n):
            if dp[i-1]>0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [-2,-1]
print(s.maxSubArray(nums))