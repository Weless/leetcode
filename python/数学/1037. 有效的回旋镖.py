from typing import List
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x,y,z = points[0],points[1],points[2]
        k1 = (y[1]-x[1])/(y[0]-x[0])
        k2 = (y[1]-z[1])/(y[0]-z[0])
        k3 = (z[1]-x[1])/(z[0]-x[0])
        return not (k1 == k2 == k3)