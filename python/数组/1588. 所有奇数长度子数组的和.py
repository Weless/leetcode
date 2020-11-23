from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        i = 0
        res = []
        while 2*i+1 <= l:
            t = 2*i+1
            j = 0
            while j+t<=l:
                res.append(arr[j:j+t])
                j+=1
            i+=1
        return sum(map(sum,res))

s = Solution()
arr = []
print(s.sumOddLengthSubarrays(arr))