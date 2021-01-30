from typing import List
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        from collections import defaultdict
        d = defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)

        t = sorted(d.items(),key=lambda x:len(x[1]),reverse=True)
        print(t)
        s1 = t[0][1]
        v = len(s1)
        res = s1[-1] - s1[0] + 1 if len(s1) > 1 else 1
        print(res)
        i = 1
        while i < len(d):
            s2 = t[i][1]
            if len(s2) == v:
                h = s2[-1] - s2[0] + 1 if len(s2) > 1 else 1
                res = min(res,h)
            else:
                break
            i+=1
        return res

s = Solution()
nums = [1,2,2,1,2,1,1,1,1,2,2,2]
print(s.findShortestSubArray(nums))


