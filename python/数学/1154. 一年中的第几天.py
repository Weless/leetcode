class Solution:
    def dayOfYear(self, date: str) -> int:
        Y,M,D = list(map(int,date.split('-')))
        ans = 0
        for m in range(M):
            if m in [1,3,5,7,8,10,12]:
                ans += 31
            elif m in [4,6,9,11]:
                ans += 30
            elif m == 0:
                continue
            else:
                if self.checkLeapYear(Y):
                    ans += 29
                else:
                    ans += 28
        ans += D
        return ans

    def checkLeapYear(self, Y):
        if Y % 400 == 0:
            return True
        if Y % 4 == 0 and Y % 100 != 0:
            return True
        return False