from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        times = len(arr) / 4
        hasCount = []
        for i in arr:
            if i not in hasCount:
                if arr.count(i) > times:
                    return i
                else:
                    hasCount.append(i)
        return -1

s = Solution()
arr = [1,2,2,6,6,6,6,7,10]
print(s.findSpecialInteger(arr))


class Solution2():
    def findSpecialInteger(self, arr: List[int]) -> int:
        import collections
        counter = collections.Counter(arr)
        return counter.most_common(1)[0][0]
s2 = Solution2()
print(s2.findSpecialInteger(arr))


# 二分查找
import  bisect
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1
s = Solution()
arr = [1,2,2,6,6,6,6,7,10]
print(s.findSpecialInteger(arr))