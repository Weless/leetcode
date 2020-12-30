from typing import List
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1]-arr[0])//len(arr)
        i = 0
        while i < len(arr)-1:
            if arr[i] + d != arr[i+1]:
                return arr[i]+d
            i+=1
