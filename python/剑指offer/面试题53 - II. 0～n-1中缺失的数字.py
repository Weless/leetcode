from typing import List

# 集合
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums) + 1
#         return (set(range(n))-set(nums)).pop()

# 遍历
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i


s = Solution()
test = [0,1,2,3,4,5,6,7,9]
print(s.missingNumber(test))