class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M in [1,3,5,7,8,10,12]:
            return 31
        if M in [4,6,9,11]:
            return 30
        if self.checkLeapYear(Y):
            return 29
        else:
            return 28
    def checkLeapYear(self,Y):
        if Y % 400 == 0:
            return True
        if Y % 4 == 0 and Y % 100 != 0:
            return True
        return False