from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:(x[0],x[1]))
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                return False
            i+=1
        return True
s = Solution()
interval = [[0,30],[5,10],[15,20]]
print(s.canAttendMeetings(interval))
