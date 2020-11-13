from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i,j = 0,len(A)-1
        while i<len(A):
            if A[i]%2 != 0:
                while j>=0 and A[j]%2 != 0:
                    j-=2
                A[i],A[j] =A[j],A[i]
            i+=2
        return A
s = Solution()
A = [4,2,5,7]
print(s.sortArrayByParityII(A))






