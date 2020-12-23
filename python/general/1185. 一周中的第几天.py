class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971年1月1日为星期五
        res = ["Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        days = 0
        for y in range(1971,year):
            if self.isLeapYear(y):
                days += 366
            else:
                days += 365
        for m in range(1,month):
            if m == 2:
                if self.isLeapYear(year):
                    days += 29
                    continue
                else:
                    days += 28
            elif m in [1,3,5,7,8,10,12]:
                days += 31
            else:
                days += 30
        days += day
        return res[days%7]



    def isLeapYear(self,year):
        if year % 400 == 0: return True
        if year % 4 == 0 and year % 100 != 0: return True
        return False
