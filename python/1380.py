from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = []
        for row in matrix:
            row_min.append(min(row))

        col_max = []
        for col in zip(*matrix):
            col_max.append(max(col))

        return [x for x in row_min if x in col_max]

s = Solution()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(s.luckyNumbers(matrix))


# 优雅的解法
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = {min(rows) for rows in matrix}
        maxes = {max(columns) for columns in zip(*matrix)}
        return list(mins & maxes)
