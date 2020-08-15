class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        s1,s2,s3=1,2,4
        for i in range(4,n):
            s1,s2,s3 = s2,s3,(s1+s2+s3)%1000000007
        return s3