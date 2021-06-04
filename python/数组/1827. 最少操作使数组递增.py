from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                continue
            res += nums[i-1]+1-nums[i]
            nums[i] = nums[i-1]+1
        return res

s = Solution()
nums = [1,5,2,4,1]
print(s.minOperations(nums))