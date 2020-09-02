class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i in S:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
        return "".join(stack)

s = Solution()
S = "abbaca"
print(s.removeDuplicates(S))