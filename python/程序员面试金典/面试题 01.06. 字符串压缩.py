class Solution:
    def compressString(self, S: str) -> str:
        comStr = ''
        i = 0
        while i < len(S):
            j = i+1
            while j < len(S) and S[j] == S[i]:
                j+=1
            n = j-i
            comStr += S[i] + str(n)
            i = j
        # print(comStr)
        if len(comStr) >= len(S):
            return S
        return comStr
s = Solution()
S = "aabcccccaaa"
print(s.compressString(S))



