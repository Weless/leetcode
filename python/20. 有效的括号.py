class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if stack:
                    x = stack.pop()
                    if (i == ')' and x == '(') or (i == ']' and x == '[') or (i == '}' and x == '{'):
                        continue
                    else:
                        return False
                else:
                    return False
        if not stack:
            return False
        return True
