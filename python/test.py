from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <=2 :
            return False
        if max(A) == A[0] or max(A) == A[-1]:
            return False
        i,j = 0,len(A)-1
        while i<len(A):
            if A[i] < A[i+1]:
                i+=1
            else:
                break
        while j>0:
            if A[j] < A[j-1]:
                j-=1
            else:
                break
        if i == j:
            return True
        return False

s = Solution()
A= [0,1,2,3,4,5,6,7,8,9]
print(s.validMountainArray(A))


