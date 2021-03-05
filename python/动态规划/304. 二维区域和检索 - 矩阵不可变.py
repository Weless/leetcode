# 前缀和
from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        m,n=len(matrix),len(matrix[0])
        self.dp = [[0 for _ in range(n)] for _ in range(m)]
        self.dp[0][0] = matrix[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    continue
                elif i == 0:
                    self.dp[i][j] += matrix[i][j] + self.dp[i][j-1]
                elif j == 0:
                    self.dp[i][j] += matrix[i][j] + self.dp[i-1][j]
                else:
                    self.dp[i][j] += matrix[i][j] + self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 != 0 and row1 != 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1] - self.dp[row1-1][col2] + self.dp[row1-1][col1-1]
        elif row1 == 0 and col1 == 0:
            return self.dp[row2][col2]
        elif row1 == 0:
            return self.dp[row2][col2] - self.dp[row2][col1-1]
        elif col1 == 0:
            return self.dp[row2][col2] - self.dp[row1-1][col2]
if __name__ == '__main__':
    matrix  = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
    n = NumMatrix(matrix)
    print(n.sumRegion(2,1,4,3))
    print(n.sumRegion(1,1,2,2))
    print(n.sumRegion(1,2,2,4))
    print(n.sumRegion(0,0,2,4))
#     matrix = [[-4,-5]]
#     n = NumMatrix(matrix)
#     print(n.sumRegion(0,0,0,0))
#     print(n.sumRegion(0,0,0,1))
#     print(n.sumRegion(0,1,0,1))