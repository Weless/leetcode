from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        if not rectangles:
            return 0
        res = []
        for item in rectangles:
            res.append(min(item))
        return res.count(max(res))
s = Solution()
rectangles = [[2,3],[3,7],[4,3],[3,7]]
print(s.countGoodRectangles(rectangles))
