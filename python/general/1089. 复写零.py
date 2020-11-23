from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if arr.count(0) == 0:
            return arr
        res = []
        for i in arr:
            if i != 0:
                res.append(i)
            else:
                res.append(0)
                if len(arr) != len(res):
                    res.append(0)
                else:
                    break
            if len(arr) == len(res):
                break

        i = 0
        while i< len(arr):
            arr[i] = res[i]
            i+=1

