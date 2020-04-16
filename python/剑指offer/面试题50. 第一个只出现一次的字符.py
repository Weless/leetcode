class Solution:
    def firstUniqChar(self, s: str) -> str:
        aMap = dict()
        for i in s:
            if i not in aMap.keys():
                aMap[i]=1
            else:
                aMap[i]+=1
        for key,value in aMap.items():
            if value == 1:
                return key
        return " "
s = Solution()
test = "abaccdeff"
print(s.firstUniqChar(test))