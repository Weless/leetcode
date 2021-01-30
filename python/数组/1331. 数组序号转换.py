from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = dict()
        i= 1
        for v in sorted(arr):
            if v not in d:
                d[v]=i
                i+=1
        res = []
        for i in arr:
            res.append(d[i])
        return res


s = Solution()
arr = [37,12,28,9,100,56,80,5,12]
print(s.arrayRankTransform(arr))

