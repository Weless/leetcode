from typing import List
# 先把所有和边界相接的陆地淹没，剩下的就是飞陆了
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(i,j):
            if not 0<=i<len(A) or not 0<=j<len(A[0]):
                return
            if A[i][j] == 1:
                A[i][j] = 0
            else:
                return
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        m,n  = len(A),len(A[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and A[i][j] == 1:
                    dfs(i,j)
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    count +=1
        return count

class Solution2:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def numEnclaves(self, A: List[List[int]]) -> int:
        from collections import deque
        m,n=len(A),len(A[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and A[i][j] == 1:
                    queue = deque()
                    queue.appendleft((i,j))
                    A[i][j] = 0
                    while queue:
                        x,y = queue.pop()
                        for direction in self.directions:
                            new_x = direction[0] + x
                            new_y = direction[1] + y
                            if 0<=new_x<m and 0<=new_y<n and A[new_x][new_y] == 1:
                                queue.appendleft((new_x,new_y))
                                A[new_x][new_y] = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 :
                    count+=1
        return count

s = Solution2()
A = [
    [0,1,1,0,0,0,0,1,1,0,0,0],
    [1,0,1,1,1,0,1,0,1,1,1,0],
    [1,1,0,1,0,0,1,1,0,1,1,1],
    [1,0,0,1,1,0,1,0,1,0,1,0],
    [1,0,0,0,0,1,0,0,1,1,0,1],
    [1,1,1,0,0,0,1,0,0,1,1,1],
    [1,1,1,0,0,0,0,1,0,1,0,1],
    [0,1,1,1,1,0,0,1,1,0,0,0],
    [0,1,0,1,0,1,0,1,0,0,0,1],
    [0,0,1,0,1,1,0,0,0,1,1,1]
]
print(s.numEnclaves(A))