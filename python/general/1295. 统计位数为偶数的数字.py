from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count =0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count +=1
        return count

s = Solution()
nums = [12,324,2,6,7896]
print(s.findNumbers(nums))