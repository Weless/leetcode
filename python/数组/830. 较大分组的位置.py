from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i=0
        res = []
        while i<len(s)-1:
            j = i+1
            while j<len(s):
                if s[j] == s[i]:
                    j+=1
                else:
                    break
            if j-i>=3:
                res.append([i,j-1])
            i = j
        return res

s = Solution()
test = "abcdddeeeeaabbbcd"
print(s.largeGroupPositions(test))