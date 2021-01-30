from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        dy = coordinates[1][1] - coordinates[0][1]
        dx = coordinates[1][0] - coordinates[0][0]
        i = 1
        while i < len(coordinates):
            dxi = coordinates[i][0] - coordinates[0][0]
            dxj = coordinates[i][1] - coordinates[0][1]
            if dy * dxi != dx * dxj:
                return False
            i+=1
        return True