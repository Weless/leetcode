from typing import List
# 原地置换法
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


s = Solution()
test = [2, 3, 1, 0, 2, 5, 3]
print(s.findRepeatNumber(test))