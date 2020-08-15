from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        i,j = 0, len(matrix[0])-1
        while i < len(matrix) and j>=0:
            if target > matrix[i][j]:
                i+=1
            elif target < matrix[i][j]:
                j-=1
            else:
                return True
        return False

s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(s.findNumberIn2DArray(matrix,target))