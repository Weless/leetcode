from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0 for i in range(len(gain)+1)]
        for i in range(len(gain)):
            res[i+1] = res[i] + gain[i]
        return max(res)
s = Solution()
gain = [-4,-3,-2,-1,4,3,2]
print(s.largestAltitude(gain))
