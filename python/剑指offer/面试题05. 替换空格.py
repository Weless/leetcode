class Solution:
    def replaceSpace(self, s: str) -> str:
        result = ''
        for i in s:
            if i != " ":
                result += i
            else:
                result += "%20"
        return result

class Solution2:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20",-1)



class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == " ":
                res.append("%20")
            else:
                res.append(i)
        return "".join(res)
s = Solution2()
test = "We are happy."
print(s.replaceSpace(test))