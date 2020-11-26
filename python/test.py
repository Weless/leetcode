from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x:x[0])
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1],interval[1])
        return ans

s = Solution()
intervals = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]
print(s.merge(intervals))







