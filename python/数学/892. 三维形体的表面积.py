from typing import List
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        x,y,z = 0,0,0
        ti = [0 for _ in range(m)]
        tj = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    x+=1
                ti[i] = max(ti[i],grid[i][j])
                tj[j] = max(tj[j],grid[i][j])
        y = sum(ti)
        z = sum(tj)
        return 2*(x+y+z)
s = Solution()
grid = [[1,2],[3,4]]
print(s.surfaceArea(grid))