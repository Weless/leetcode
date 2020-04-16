class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        id = len(S) -1
        result = ''
        for v in S:
            if v.isalpha():
                while not S[id].isalpha():
                    id -= 1
                result += S[id]
                id -=1
            else:
                result += v
        return result

s = Solution()
test = "Test1ng-Leet=code-Q!"
print(s.reverseOnlyLetters(test))


## 字母栈
class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)
