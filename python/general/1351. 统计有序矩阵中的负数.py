from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for x in grid:
            for y in x:
                if y <0:
                   count+=1
        return count

s = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(s.countNegatives(grid))