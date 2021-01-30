from typing import List
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A.reverse()
        t = 0
        i = 0
        while K != 0:
            K,m = K//10,K%10
            A[i] = A[i] + m + t
            if A[i] >= 10 :
                A[i]-=10
                t = 1
            else:
                t = 0
            i+=1
        while t == 1:
            if i < len(A):
                A[i]+=1
                if A[i] >= 10:
                    A[i] -= 10
                    t = 1
                else:
                    t = 0
            else:
                break
            i+=1
        if t == 1:
            A.append(1)
        A.reverse()
        return A
        # return list(A.reverse())

s = Solution()
A = [9,9,9]
K = 1
print(s.addToArrayForm(A,K))