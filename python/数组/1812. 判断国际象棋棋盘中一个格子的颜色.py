class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        matrix = [[1 for _ in range(8)] for _ in range(8)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i % 2 == 0:
                    if j % 2 == 0:
                        matrix[i][j] = 0
                else:
                    if j % 2 != 0:
                        matrix[i][j] = 0
        d = {
            "a":0,
            "b":1,
            "c":2,
            "d":3,
            "e":4,
            "f":5,
            "g":6,
            "h":7
        }
        x,y = int(coordinates[1])-1,d[coordinates[0]]
        return True if matrix[x][y] else False

# 异或操作
class Solution:
    def squareIsWhite(self, coordinates):
        stage = (ord(coordinates[0]) - ord('a')) % 2
        num = (int(coordinates[1]) - 1) % 2
        return True if stage ^ num else False
