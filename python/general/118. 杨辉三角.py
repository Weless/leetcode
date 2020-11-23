from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        res = [[1]*i for i in range(1,numRows+1)]
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == 0 or j == len(res[i])-1:
                    continue
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
