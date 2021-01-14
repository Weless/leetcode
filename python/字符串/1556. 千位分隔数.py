class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        str_n = str(n)
        i = len(str_n)-1
        res = []
        c = 0
        while i>=0:
            res.append(str_n[i])
            c+=1
            if c==3:
                res.append(".")
                c=0
            i-=1
        # print(res[::-1])
        return ''.join(list(res[::-1])).lstrip(',')
s = Solution()
print(s.thousandSeparator(12345))
