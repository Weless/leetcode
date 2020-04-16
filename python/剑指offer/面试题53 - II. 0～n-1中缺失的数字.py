from typing import List

# 集合
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) + 1
#         return (set(range(n))-set(nums)).pop()

# 遍历
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                return nums[i]+1
        return nums[-1]+1

s = Solution()
test = [0,1,2,3,4,5,6,7,9]
print(s.missingNumber(test))