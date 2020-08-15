from typing import List
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        timeList = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        def dfs(start,path,timeList):
            if len(path) == num:
                res.append(path[:])
                return
            for i in range(start,len(timeList)):
                if timeList[i] in path:
                    continue
                path.append(timeList[i])
                dfs(i,path,timeList)
                path.pop()
        res = []

        dfs(0,[],timeList)
        def mySum(*times):
            t_hour, t_minute = 0,0
            for time in times[0]:
                hour,mimute = time.split(':')
                t_hour+=int(hour)
                t_minute+=int(mimute)
            if t_minute >= 60 or t_hour>=12:
                return ''
            return str(t_hour) + ":" + "{:0>2d}".format(t_minute)
        return [i for i in list(map(mySum,res)) if i != ""]

s = Solution()
n = 2
print(s.readBinaryWatch(n))