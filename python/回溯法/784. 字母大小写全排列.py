from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(s,index):
            if index == len(s):
                res.append(''.join(s))
                return
            if s[index].isdigit():
                dfs(s,index+1)
            else:
                dfs(s,index+1)
                # s[index] = s[index].swapcase()
                s[index] = chr(ord(s[index])^32)
                dfs(s,index+1)
        res = []
        s = list(S)
        dfs(s, 0)
        return res

s = Solution()
S = "A1B2"
print(s.letterCasePermutation(S))