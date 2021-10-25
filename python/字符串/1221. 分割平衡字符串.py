class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        count = 0
        for i in s:
            if i == "R":
                num +=1
            else:
                num -= 1
            if num == 0:
                count +=1
        return count
s = Solution()
test = "RLRRRLLRLL"
print(s.balancedStringSplit(test))