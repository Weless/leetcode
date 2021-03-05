from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix: return True
        m,n = len(matrix),len(matrix[0])
        tmp = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_i = i+1
                new_j = j+1
                if new_i < m and new_j < n and matrix[new_i][new_j] != matrix[i][j]:
                    return False
        return True