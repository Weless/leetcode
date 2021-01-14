from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        d = dict(Counter(nums))
        tmp = sorted(d.items(),key=lambda x:(x[1],-x[0]))
        print(tmp)
        res = []
        for i,j in tmp:
            res+=[i]*j
        return res

s = Solution()
nums = [2,3,1,3,2]
print(s.frequencySort(nums))
