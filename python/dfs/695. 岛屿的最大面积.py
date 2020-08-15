from typing import List
class Solution:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque()
        m,n = len(grid),len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 0
                    queue.appendleft((i,j))
                    grid[i][j] = 0
                    while queue:
                        count += 1
                        x,y = queue.pop()
                        for direction in self.directions:
                            new_x = x + direction[0]
                            new_y = y + direction[1]
                            if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == 1:
                                queue.appendleft((new_x,new_y))
                                grid[new_x][new_y] = 0
                    res = max(res,count)
        return res

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1)
        m,n = len(grid),len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res


s = Solution2()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.maxAreaOfIsland(grid))