from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

# 空间复杂度O(1)
# 先记录第一行第一列是否有0，然后利用第一行第一列作为标记，先清除非第一行或非第一列的数据，最后根据第一列第一列是否有0来清除第一行第一列
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        isFirstRowHaveZero = False
        isFirstColHaveZero = False
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstColHaveZero = True

        for i in range(n):
            if matrix[0][i] == 0:
                isFirstRowHaveZero = True

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[0][j] == 0 or matrix[i][0] ==0:
                    matrix[i][j] = 0

        for i in range(m):
            if isFirstColHaveZero:
                matrix[i][0] = 0

        for i in range(n):
            if isFirstRowHaveZero:
                matrix[0][i] = 0
