from typing import List
# 超时
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        i = 0
        while i < len(nums):
            d = {
                0:0,1:0
            }
            d[nums[i]]+=1
            j = i+1
            while j < len(nums):
                d[nums[j]]+=1
                if d[0] == d[1]:
                    max_len = max(max_len,j-i+1)
                j+=1
            i+=1
        return max_len
# 前缀和


s = Solution()
nums = [0,0,1,0,0,0,1,1]
print(s.findMaxLength(nums))
