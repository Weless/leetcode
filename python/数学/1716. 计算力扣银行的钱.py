class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        week = 0
        while n != 0:
            if n>=7:
                res += week*7+(1+2+3+4+5+6+7)
                n-=7
            else:
                res+= week*n
                while n != 0:
                    res+=n
                    n-=1
            week+=1
        return res