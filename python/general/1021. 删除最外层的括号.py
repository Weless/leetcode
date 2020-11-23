class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        tmpStr = ''
        if S == '':
            return ''
        stack = []
        for i in S:
            if i == '(':
                stack.append(i)
                if len(stack) != 1:
                    tmpStr += i
            else:
                stack.pop()
                if len(stack) != 0:
                    tmpStr += i
        return tmpStr


s = Solution()
print(s.removeOuterParentheses("(()())(())(()(()))"))
print(s.removeOuterParentheses("(()())(())"))
print(s.removeOuterParentheses("()()"))



#### other answer

'''
def removeOuterParentheses(self, S):
    res, opened = [], 0
    for c in S:
        if c == '(' and opened > 0: res.append(c)
        if c == ')' and opened > 1: res.append(c)
        opened += 1 if c == '(' else -1
    return "".join(res)
'''
