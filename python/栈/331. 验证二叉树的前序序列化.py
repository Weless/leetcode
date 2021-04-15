class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [1]
        i = 0
        while i < len(preorder):
            if not stack: break
            if preorder[i] == ',':
                i+=1
            elif preorder[i] == '#':
                stack[-1]-=1
                if stack[-1] == 0:
                    stack.pop()
                i+=1
            else:
                while i<len(preorder) and preorder[i] != ',':
                    i+=1
                stack[-1]-=1
                if stack[-1] == 0:
                    stack.pop()
                stack.append(2)
        return not stack

s = Solution()
preorder = "9,#,92,#,#"
print(s.isValidSerialization(preorder))