class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j= 0,0
        res = ''
        while i<len(word1) or j < len(word2):
            if i < len(word1):
                if i == j:
                    res+=word1[i]
                    i+=1
                else:
                    res+=word1[i:]
                    break

            if j < len(word2):
                if i == j+1:
                    res+=word2[j]
                    j+=1
                else:
                    res+=word2[j:]
                    break
        return res
s = Solution()
word1 = ""
word2 = "pqr"
print(s.mergeAlternately(word1,word2))
