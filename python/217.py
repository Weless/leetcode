from typing import List
class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        import heapq
        if len(nums) == 0:
            return False
        heapq.heapify(nums)
        print(nums)
        i = 0
        while i <= len(nums) -2 :
            if nums[i] == nums[i+1]:
                return True
        return False

s = Solution()
test = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(test))