from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[(0+len(nums))//2]

s = Solution()
test = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(s.majorityElement(test))