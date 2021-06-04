
class Solution:
    alpha = "abcdefghijklmnopqrstuvwxyz"
    def replaceDigits(self, s: str) -> str:
        tmp = []
        i = 0
        while i<len(s):
            if i+1 <len(s):
                tmp.append((s[i],s[i+1]))
            else:
                tmp.append((s[i],-1))
            i+=2
        res = ''
        for i,j in tmp :
            res+=i
            if j != -1:
                res+=self.shift(i,int(j))
        return res

    def shift(self,a,t):
        for i,v in enumerate(self.alpha):
            if v == a:
                return self.alpha[i+t]

s = Solution()
test = "a1b2c3d4e"
print(s.replaceDigits(test))