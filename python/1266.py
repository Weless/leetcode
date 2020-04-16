from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i,v in enumerate(points):
            if i == 0:
                continue
            last = i - 1
            count += max(abs(v[1]-points[last][1]),abs(v[0]-points[last][0]))
        return count

s = Solution()
points = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(points))