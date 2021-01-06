from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1 or not nums:
            return 0
        nums.sort()
        res = -1
        for i in range(len(nums)-1):
            j = i+1
            res = max(abs(nums[j] -nums[i]),res)
        return res
s = Solution()
nums = [3,6,9,1]
print(s.maximumGap(nums))