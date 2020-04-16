from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1 :
            return ["()"]
        if n > 1:
            alist = self.generateParenthesis(n-1)
            result = []
            for item in alist:
                result.append("()" + item)
                result.append("(" + item + ")")
                result.append(item + "()")
            if n % 2 ==0:
                result.append("(())"*(n//2))
            return list(set(result))
s = Solution()
n = 4
print(s.generateParenthesis(4))

