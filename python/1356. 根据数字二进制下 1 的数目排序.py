from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        from collections import defaultdict
        arr.sort()
        d = defaultdict(list)
        for i in arr:
            n = bin(i).count('1')
            d[n].append(i)
        res = []
        for i in sorted(d):
            res.extend(d[i])
        return res

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x:(bin(x).count('1'),x))
        return arr

s = Solution()
arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(s.sortByBits(arr))