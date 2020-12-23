class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        i = 0
        ans = 0
        while i < len(s):
            j = i+1
            tmp = ''
            if j < len(s):
                tmp = s[i] + s[j]
                if tmp in d:
                    ans += d[tmp]
                    i+=2
                else:
                    tmp = s[i]
                    ans += d[tmp]
                    i+=1
            else:
                tmp = s[i]
                ans += d[tmp]
                i+=1
        return ans
s = Solution()
test = "MCMXCIV"
print(s.romanToInt(test))
