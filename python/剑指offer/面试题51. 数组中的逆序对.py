from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        while j >=0:
            i = 0
            count = 0
            while i < j:
                if nums[i] > nums[j]:
                    count+=1
                i+=1
            nums[j] = count
            j-=1
        return sum(nums)

s = Solution()
nums = [7,5,6,4]
print(s.reversePairs(nums))