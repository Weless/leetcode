from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = len(nums)-1
        count = 0
        def helper(i,j):
            _count = 0
            while i<j:
                if nums[i] % 2 != 0:
                    _count+=1
                i+=1
            if _count == k:
                return True
            return False
        while j-i>=k:
            count += 1 if helper(i,j) else count
            i+=1
        return count
s = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(s.numberOfSubarrays(nums,k))