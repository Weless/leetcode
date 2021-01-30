class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        totol_string = ''
        for i in S:
            if i.isalpha():
                totol_string+=i.upper()
            elif i == '-':
                continue
            else:
                totol_string+=i

        a,b = divmod(len(totol_string),K)
        if b != 0:
            a+=1
        print(totol_string,a,b)
        i = 0
        res = []
        last = 0
        while i < a:
            if i == 0 and b != 0:
                res.append(totol_string[0:b])
                last = b
            else:
                res.append(totol_string[last:last+K])
                last = last+K
            i+=1
        print(res)
        return '-'.join(res)
s = Solution()
S = "2-5g-3-J"
K = 2
print(s.licenseKeyFormatting(S,K))