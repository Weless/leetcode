# 思路1：栈
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1,stack2 = [],[]
        self.help(S,stack1)
        self.help(T,stack2)
        # print(stack1,stack2)
        return stack1 == stack2
    def help(self,A,stack):
        for i in A:
            if i == '#':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)

# 思路2：倒序遍历



s = Solution()
S = "a#c"
T = "b"
print(s.backspaceCompare(S,T))