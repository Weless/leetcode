from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ''
        first = strs[0]
        exist = True
        for i in first:
            result += i
            for word in strs[1:]:
                if not word.startswith(result):
                    exist = False
                    break
            if not exist:
               return result[:-1]
        return result

s = Solution()
alist = ["flower","flow","flight"]
alist2 = ["dog","racecar","car"]
print(s.longestCommonPrefix(alist2))
