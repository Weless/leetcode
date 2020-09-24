class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        if n < 10:
            return n
        d = defaultdict(list)
        lmax = 0
        anx = 0
        for i in range(1,n+1):
            t = self.calculate(i)
            d[t].append(i)
            lmax = max(lmax,len(d[t]))
        for v in d.values():
            if len(v) == lmax:
                anx +=1
        return anx

    def calculate(self,num):
        r = 0
        while num:
            r += num % 10
            num //= 10
        return r

s = Solution()
n = 15
print(s.countLargestGroup(n))

