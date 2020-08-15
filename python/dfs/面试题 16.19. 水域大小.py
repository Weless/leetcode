from typing import List
class Solution:
    directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land:
            return []
        from collections import deque
        queue = deque()
        m,n = len(land),len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 :
                    queue.appendleft((i,j))
                    land[i][j] = 1
                    count = 0
                    while queue:
                        count +=1
                        x,y = queue.pop()
                        for direction in self.directions:
                            new_x = x + direction[0]
                            new_y = y + direction[1]
                            if 0<=new_x<m and 0<=new_y<n and land[new_x][new_y] == 0:
                                queue.appendleft((new_x,new_y))
                                land[new_x][new_y] = 1
                    res.append(count)
        return sorted(res)

class Solution2:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land:
            return []
        def dfs(i,j):
            if not 0<=i<len(land) or not 0<=j<len(land[0]) or land[i][j] != 0:
                return 0
            land[i][j] = 1
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)+dfs(i-1,j-1)+dfs(i+1,j-1)+dfs(i+1,j+1)+dfs(i-1,j+1)
        res = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    res.append(dfs(i,j))
        return sorted(res)



s = Solution2()
land = [
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
print(s.pondSizes(land))