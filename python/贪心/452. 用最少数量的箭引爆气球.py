from typing import List

# 贪心算法的思想：
# 在保证射中当前气球的情况下，总是将箭的坐标延伸至可以射中下一个气球的最远位置！

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # 按照右边界排序
        points.sort(key=lambda balloon: balloon[1])
        print(points)
        pos = points[0][1]         # 当前箭射出的位置
        ans = 1
        for balloon in points:     # 遍历所有气球
            if balloon[0] > pos:   # 找出右边界位置最靠左边的气球
                pos = balloon[1]   # 更新右边界：下一只箭射出的位置
                ans += 1           # 射爆
        return ans


s = Solution()
points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(s.findMinArrowShots(points))

