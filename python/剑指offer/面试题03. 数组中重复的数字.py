from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                return nums[i]
            i+=1

s = Solution()
test = [2, 3, 1, 0, 2, 5, 3]
print(s.findRepeatNumber(test))