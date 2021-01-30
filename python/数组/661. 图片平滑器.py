from typing import List
class Solution:
    direcitions = [(1,1),(1,0),(0,1),(0,0),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)]
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

    def helper(self,M,x,y):
        m,n = len(M),len(M[0])
        t =
        for i,j in self.direcitions:
            new_x = i + x
            new_y = j + y
            if 0<=new_x<=m and 0<=new_y<=n:
