from typing import List
class Solution:
    directions = [(1,0),(0,1)]
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m,n = len(matrix),len(matrix[0])
        if n == 0:
            return False
        from collections import deque
        queue = deque()
        queue.append((0,0))
        mark = [[False for _ in range(n)] for _ in range(m)]
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                mark[x][y] = True
                if matrix[x][y] == target:
                    return True
                else:
                    for directions in self.directions:
                        new_x = directions[0] + x
                        new_y = directions[1] + y
                        if 0<=new_x<=m-1 and 0<=new_y<=n-1 and not mark[new_x][new_y]:
                            queue.append((new_x,new_y))
        return False

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(s.findNumberIn2DArray(matrix,target))