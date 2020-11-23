from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        i,j = 0 ,len(height)-1
        res = 0
        while i <= j:
            area = (j-i) * min(height[i],height[j])
            res = max(res,area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return res
s = Solution()
array = [1,8,6,2,5,4,8,3,7]
print(s.maxArea(array))