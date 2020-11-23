from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 0:
            return False
        aMap = {}
        for id,v in enumerate(nums):
            if v not in aMap.keys():
                aMap[v] = id
            else:
                if id - aMap[v] <= k:
                    return True
                else:
                    aMap[v] = id
        return False
s = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums,k))