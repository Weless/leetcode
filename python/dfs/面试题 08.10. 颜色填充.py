from typing import List
# BFS
class Solution:
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        queue = deque()
        queue.appendleft((sr,sc))
        color = image[sr][sc]
        m,n = len(image),len(image[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        while queue:
            x,y = queue.pop()
            image[x][y] = newColor
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0<=new_x<m and 0<=new_y<n and marked[new_x][new_y] == False and image[new_x][new_y] == color:
                    queue.appendleft((new_x,new_y))
                    marked[new_x][new_y] = True
        return image

# DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(i,j):
            if not 0<=i<len(image) or not 0<=j<len(image[0]) or image[i][j] != color or color == newColor:
                return
            image[i][j] = newColor
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        color = image[sr][sc]
        dfs(sr,sc)
        return image