from typing import List
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for i in A:
            for key in d.keys():
                if self.checkIsEuqual(i,key):
                    d[key]+=1
                    break
            else:
                d[i] = 0
        return len(d)
    def checkIsEuqual(self,A,B):
        if len(A) != len(B):
            return False
        odd = set()
        even = set()
        i = 0
        while i < len(A):
            if i % 2 == 0:
                even.add(A[i])
            else:
                odd.add(A[i])
            i+=1
        i = 0
        while i < len(B):
            if i % 2 == 0:
                if B[i] not in even:
                    return False
            else:
                if B[i] not in odd:
                    return False
            i+=1
        return True
s = Solution()
A = ["ababaa","aaabaa"]
print(s.numSpecialEquivGroups(A))