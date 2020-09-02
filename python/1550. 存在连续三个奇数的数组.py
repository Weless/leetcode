from typing import List
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i,v in enumerate(arr):
            res = 0
            if v & 1:
                res+=1
                j = i+1
                while j < len(arr):
                    if arr[j] & 1 :
                        res +=1
                        if res == 3:
                            return True
                    else:
                        break
                    j+=1
        return False

s = Solution()
arr = [2,6,4,1]
print(s.threeConsecutiveOdds(arr))

