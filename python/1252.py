from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        alist = [[0]*m for _ in range(n)]
        # print(alist)

        for x,y in indices:
            for i in range(n):
                alist[i][y] += 1
            for j in range(m):
                alist[x][j] += 1
        print(alist)
        return sum(elem % 2 == 1 for line in alist for elem in line)


s = Solution()
n = 2
m = 3
indices = [[0,1],[1,1]]
print(s.oddCells(n,m,indices))
