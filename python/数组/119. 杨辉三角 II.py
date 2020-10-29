from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1] * i for i in range(1, rowIndex + 2)]
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == 0 or j == len(res[i]) - 1:
                    continue
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res[rowIndex]

## better
# 根据上一行推出下一行
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            res.insert(0, 0)
            for j in range(len(res)-1):
                res[j] = res[j] + res[j+1]
        return res
s = Solution()
n = 3
print(s.getRow(n))
