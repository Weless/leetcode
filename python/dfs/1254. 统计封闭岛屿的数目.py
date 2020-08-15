from typing import List
# BFS
class Solution:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def closedIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        m,n = len(grid),len(grid[0])
        queue = deque()
        marked = [[False for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 0:
                    continue
                if grid[i][j] == 0 and marked[i][j] == False:
                    tag = 0
                    queue.appendleft((i,j))
                    while queue:
                        x,y = queue.pop()
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            tag = 1
                        for direction in self.directions:
                            new_x = x + direction[0]
                            new_y = y + direction[1]
                            if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == 0 and marked[new_x][new_y] == False:
                                queue.appendleft((new_x,new_y))
                                marked[new_x][new_y] = True
                    if tag == 0:
                        res+=1
        return res

# DFS
class Solution2:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if not 0<=i<len(grid) or not 0<=j<len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            left = dfs(i,j-1)
            right = dfs(i,j+1)
            up = dfs(i-1,j)
            down = dfs(i+1,j)
            if left and right and up and down:
                return True
            else:
                return False
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        count+=1
        return count
s = Solution2()
grid = [
    [1,1,0,1,1,1,1,1,1,1],
    [0,0,1,0,0,1,0,1,1,1],
    [1,0,1,0,0,0,1,0,1,0],
    [1,1,1,1,1,0,0,1,0,0],
    [1,0,1,0,1,1,1,1,1,0],
    [0,0,0,0,1,1,0,0,0,0],
    [1,0,1,0,0,0,0,1,1,0],
    [1,1,0,0,1,1,0,0,0,0],
    [0,0,0,1,1,0,1,1,1,0],
    [1,1,0,1,0,1,0,0,1,0]
]
print(s.closedIsland(grid))