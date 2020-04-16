from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for i in intervals:
            if not res:
                res.append(i)
            else:
                if res[-1][1]>=i[0]:
                    res[-1] = [res[-1][0],max(res[-1][1],i[1])]
                else:
                    res.append(i)
        return res

s = Solution()
test = [[2,6],[1,3],[8,10],[15,18]]
test2 = [[1,4],[4,5]]
print(s.merge(test2))

