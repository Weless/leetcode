from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if m <3 or n<3:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                s = set()
                if m-i < 3 or n-j < 3:
                    break
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        s.add(grid[x][y])
                if s != set(range(1,10)):
                    continue
                a = grid[i][j] + grid[i+1][j] + grid[i+2][j]
                b = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                c = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                if a == b and a ==c:
                    res +=1
        return res
s = Solution()
grid = [[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]
print(s.numMagicSquaresInside(grid))