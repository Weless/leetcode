from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        up,down,left,right = 0,len(matrix)-1,0,len(matrix[0])-1
        cnt = 1
        while True:
            i = left
            while i <= right:
                matrix[up][i] = cnt
                i+=1
                cnt+=1
            up+=1

            if up > down:
                break

            i = up
            while i <= down:
                matrix[i][right] = cnt
                i+=1
                cnt+=1
            right -= 1

            if left > right:
                break

            i = right
            while i >= left:
                matrix[down][i] = cnt
                i-=1
                cnt+=1
            down-=1

            if up > down:
                break

            i = down
            while i >= up:
                matrix[i][left] = cnt
                i-=1
                cnt+=1
            left+=1

            if left > right:
                break
        return matrix
s = Solution()

print(s.generateMatrix(3))