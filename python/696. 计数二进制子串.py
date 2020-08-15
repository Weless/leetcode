class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = len(s)
        if l == 1 or l == 0:
            return 0
        res = 0
        i = 0
        while i < l:
            tmp = 1
            j = i+1
            while j < l:
                if s[j] == s[i]:
                    tmp +=1
                else:
                    tmp -=1
                if tmp == 0:
                    res +=1
                    break
                j+=1
            i+=1
        return res
s = Solution()
s1 = "10101"
print(s.countBinarySubstrings(s1))



