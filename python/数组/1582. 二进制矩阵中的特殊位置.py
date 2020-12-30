from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ok = True
                if mat[i][j] == 1:
                    for x in range(n):
                        if mat[i][x] == 1 and x != j:
                            ok = False
                            break
                    if not ok:
                        continue
                    for x in range(m):
                        if mat[x][j] == 1 and x != i:
                            ok = False
                            break
                    if ok:
                        ans +=1
        return ans
