from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left,right = 0,0
        while right < len(A):
            if A[right] == 0:
                K-=1
            if K < 0:
                if A[left]==0:
                    K+=1
                left+=1
            right+=1
        return right-left

s = Solution()
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(s.longestOnes(A,K))
