class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        yMap = {'a':[],'e':[],'i':[],'o':[],'u':[]}

        for index,i in enumerate(s):
            if i in ['a','e','i','o','u']:
                yMap[i].append(index)

        theMin, theMax = 0, len(s) - 1
        for k,v in yMap.items():
            if len(v) == 0:
                continue
            if len(v) == 1:
                yMap[k] = []
            if len(v) > 2:
                yMap[k] = yMap[k][:2]
                theMin = min(min(yMap[k]),theMin)
                theMax = max(max(yMap[k]),theMax)
            return s[theMin:theMax+1]
s = Solution()
test = "eleetminicoworoep"
print(s.findTheLongestSubstring(test))



