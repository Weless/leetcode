from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = dict()
        for i in arr1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        arr1.sort()
        tmp = []
        for i in arr1:
            if i not in arr2:
                tmp.append(i)
        res = []
        for i in arr2:
            res += [i]*d[i]
        return res + tmp

s = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(s.relativeSortArray(arr1,arr2))


