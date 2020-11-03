from typing import List
class Solution:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid: return res
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += self.count(i,j,m,n,grid)
        return res

    def count(self,x,y,m,n,grid):
        res = 4
        for d in self.directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if 0 <= new_x <= m-1 and 0<=new_y<=n-1 and grid[new_x][new_y] == 1:
                res -=1
        return res

# dfs
class Solution2:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        self.ans = 0
        def dfs(x,y):
            if x<0 or x>=m or y <0 or y>=n or grid[x][y] == 0:
                self.ans +=1
                return
            # 标记已经访问过
            if grid[x][y] == 2:
                return
            grid[x][y] = 2
            for d in self.directions:
                dfs(x+d[0],y+d[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        return self.ans

s = Solution2()
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print(s.islandPerimeter(grid))