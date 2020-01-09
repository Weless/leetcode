class Solution:
    def minTimeToVisitAllPoints(self, points):
        total = 0
        i = 1
        while i<len(points):
            j = i - 1
            total += max([abs(points[i][0]-points[j][0]),abs(points[i][1]-points[j][1])])
            i+=1
        return total

s = Solution()
print(s.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
