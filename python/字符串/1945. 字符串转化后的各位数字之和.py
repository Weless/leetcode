class Solution:
    def getLucky(self, s: str, k: int) -> int:

        res = ""
        for i in range(len(s)):
            res += str(i+1)

        index = 0
        t = 0
        while index<k:
            tmp = 0
            for i in res:
                tmp+=int(i)
            index+=1
            t = tmp
            res = str(tmp)
        return t
s = Solution()
print(s.getLucky("iiii",1))

