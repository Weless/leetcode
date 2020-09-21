from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        from operator import itemgetter
        digit_log = []
        al_log = []
        for log in logs:
            tag, content = log.split(' ',1)
            if self.isDigitLog(content.split(' ')):
                digit_log.append(log)
            else:
                al_log.append(log)
        al_log.sort(key=lambda x: itemgetter(1,0)(x.split(" ",1)))
        return al_log + digit_log
    def isDigitLog(self, s:str):
        for i in s:
            if not i.isdigit():
                return False
        return True
s = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab3 off key dog","ab1 off key dog","a8 act zoo"]
print(s.reorderLogFiles(logs))