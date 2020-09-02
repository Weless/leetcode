class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) == 1:
            return True

        d1,d2 = dict(),dict()
        for i in A:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in B:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        if d1 != d2:
            return False

        dif = 0
        i = 0
        while i<len(A):
            if A[i] != B[i]:
                dif +=1
            if dif > 2 :return False
            i+=1
        return True if dif else False


s = Solution()
A = "ab"
B = "ba"
print(s.buddyStrings(A,B))