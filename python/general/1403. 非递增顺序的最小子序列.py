from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(set(nums)) == 1:
            return nums
        nums.sort(reverse=True)
        i = 1
        while i < len(nums):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
            i+=1
s = Solution()
nums = [4,3,10,9,8]
print(s.minSubsequence(nums))