from typing import List

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        i = 0
        count = 0
        p = [0 for _ in range(len(A))]

        while i < len(A):
            j = i + 1
            p[0] = A[i]
            while j <= len(A):
                p[j] = A[j] + p[j-1]
                if (p[j]%K==0):
                    count+=1
                j+=1
            i+=1
        return count
s = Solution()
A = [4,5,0,-2,-3,1]
K = 5
print(s.subarraysDivByK(A,K))