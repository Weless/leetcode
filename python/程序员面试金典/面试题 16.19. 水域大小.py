from typing import List
class Solution:
    directions = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        if not land:
            return []
        m,n = len(land),len(land[0])
        from collections import deque
        queue = deque()
        mark = [[False for _ in range(n)] for _ in range(m)]
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 and mark[i][j] == False:
                    queue.append((i,j))
                    mark[i][j] = True
                    count = 0
                    while queue:
                        x,y = queue.popleft()
                        count += 1
                        for position in self.directions:
                            new_x = x + position[0]
                            new_y = y + position[1]
                            if 0<=new_x<=m-1 and 0<=new_y<=n-1 and land[new_x][new_y] == 0 and mark[new_x][new_y] == False:
                                queue.append((new_x,new_y))
                                mark[new_x][new_y] = True

                    res.append(count)
        return sorted(res)

s = Solution()
land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
print(s.pondSizes(land))