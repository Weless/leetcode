from typing import List
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        i = 0
        res = arr[:]
        while True:
            ok = True
            arr = res[:]
            i = 0
            while i < len(arr):
                if i == 0 or i == len(arr)-1:
                    i+=1
                    continue
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    res[i]+=1
                    ok = False
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    res[i]-=1
                    ok = False
                i+=1
            if ok:
                break
        return res
s = Solution()
arr = [1,6,3,4,3,5]
print(s.transformArray(arr))