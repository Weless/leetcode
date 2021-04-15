from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up,down,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
        res = []
        while True:
            i = left
            while i <= right:
                res.append(matrix[up][i])
                i+=1
            up+=1

            if up > down:
                break

            i = up
            while i <= down:
                res.append(matrix[i][right])
                i+=1
            right -= 1

            if left > right:
                break

            i = right
            while i >= left:
                res.append(matrix[down][i])
                i-=1
            down-=1

            if up > down:
                break

            i = down
            while i >= up:
                res.append(matrix[i][left])
                i-=1
            left+=1

            if left > right:
                break
        return res
s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))
