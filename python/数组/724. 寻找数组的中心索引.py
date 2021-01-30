from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if 2*left+nums[i] == total:
                return i
            left+=nums[i]
        return -1
s = Solution()
nums = [1]
print(s.pivotIndex(nums))
