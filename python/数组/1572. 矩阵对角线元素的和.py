from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        res = 0
        i = 0
        while i < m:
            res += mat[i][i]
            res += mat[m - 1 - i][i]
            i+=1
        if m % 2 == 0:
            return res
        else:
            return res - mat[i//2][i//2]
s = Solution()
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(s.diagonalSum(mat))
