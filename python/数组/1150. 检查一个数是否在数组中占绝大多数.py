from typing import List
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        from collections import defaultdict
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        n = d[target]
        return True if n > len(nums)//2 else False
s = Solution()
nums = [2,4,5,5,5,5,5,6,6]
target = 5
print(s.isMajorityElement(nums,target))