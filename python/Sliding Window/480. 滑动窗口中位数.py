from typing import List
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        odd = False
        if k % 2 == 0:
            odd = False
        else:
            odd = True
        i = k-1
        res = []
        while i < len(nums):
            tmp = sorted(nums[i-k+1:i+1])
            if odd:
                res.append(tmp[len(tmp)//2])
            else:
                res.append((tmp[len(tmp)//2-1] + tmp[len(tmp)//2])/2)
            i+=1
        return res
s =  Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 4
print(s.medianSlidingWindow(nums,k))