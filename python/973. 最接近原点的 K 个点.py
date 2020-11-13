from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from math import sqrt
        points.sort(key=lambda point:sqrt(point[0]*point[0]+point[1]*point[1]))
        return points[:K]
s = Solution()
points = [[3,3],[5,-1],[-2,4]]
K = 2
print(s.kClosest(points,K))