from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 0
        matrix = [['' for _ in range(3)] for _ in range(3)]
        turn = 'A'
        for x,y in moves:
            if n > 9:
                return "Draw"
            if turn == 'A':
                matrix[x][y] = 'X'
                turn = "B"
                n+=1
                if self.checkIsWin(matrix,x,y): return "A"
            else:
                matrix[x][y] = 'O'
                turn = "A"
                n+=1
                if self.checkIsWin(matrix,x,y): return "B"
        if n == 9:
            return "Draw"
        else:
            return "Pending"

    def checkIsWin(self,matrix,x,y):
        if matrix[x][0] == matrix[x][1] and matrix[x][1] == matrix[x][2]:
            return True
        if matrix[0][y] == matrix[1][y] and matrix[1][y] == matrix[2][y]:
            return True
        if x == y:
            if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
                return True
        if (x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0):
            if matrix[1][1] == matrix[0][2] == matrix[2][0]:
                return True
        return False

s = Solution()
moves = [[0,0],[1,1]]
print(s.tictactoe(moves))