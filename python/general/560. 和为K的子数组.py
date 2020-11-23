from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        from collections import deque
        d = deque()
        i = 0
        while i<k:
            d.append(nums[i])
            i+=1
        count = 0
        if sum(d) == k:
            count +=1
        while i<len(nums):
            d.append(nums[i])
            d.popleft()
            if sum(d) == k:
                count +=1
            i+=1
        return count
s = Solution()
nums = [1,1,1]
k = 2
print(s.subarraySum(nums,k))