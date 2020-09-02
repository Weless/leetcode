class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        words = s.split()
        res = 0
        for i in words[-1]:
            if i.isalpha():
                res +=1
            else:
                return 0
        return res

s = Solution()
test = "Hello World"
print(s.lengthOfLastWord(test))