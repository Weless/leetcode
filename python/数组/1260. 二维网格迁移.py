from typing import List
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])

        for _ in range(k):
            tmp = [0] * m
            for i in range(m):
                tmp[i] = grid[i][n-1]
            for i in range(m):
                for j in range(n-1,0,-1):
                    grid[i][j] = grid[i][j-1]
            grid[0][0] = tmp[-1]
            for i in range(1,m):
                grid[i][0] = tmp[i-1]
            # print(grid)
        return grid
s = Solution()
grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(s.shiftGrid(grid,k))