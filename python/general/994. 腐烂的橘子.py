# 多源BFS
from typing import List
class Solution:
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])

        fresh = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh = True
                    break
            if fresh: # 还有新鲜橘子
                break
        else:
            return 0 # 没有新鲜橘子

        from collections import deque
        queue = deque()
        # mark = [[False for _ in range(n)] for _ in range(m)]
        steps = []

        # 一开始所有的腐烂橘子为同一层
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))

        minutes = 0
        # mark[i][j] = True
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for position in self.directions:
                    new_x = position[0] + x
                    new_y = position[1] + y
                    if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        queue.append((new_x, new_y))
                        # mark[new_x][new_y] = True
            minutes += 1
        minutes -=1 # 最后一个橘子已经腐烂，入队、出队不计


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return minutes

s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
grid3 = [[0,2]]
grid4 = [[2],[1],[1],[1],[2],[1],[1]]
print(s.orangesRotting(grid4))