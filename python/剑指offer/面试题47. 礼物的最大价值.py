from typing import List
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = max(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
s = Solution()
input = [
  [1]
]
print(s.maxValue(input))