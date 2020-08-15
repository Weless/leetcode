class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            return s == s[::-1]

        strPart = lambda s, x: s[:x] + s[x + 1:]
        i, j = 0, len(s) - 1
        while i<j:
            if s[i] != s[j]:
                return helper(strPart(s,i)) or helper(strPart(s,j))
            i+=1
            j-=1
        return True

s = Solution()
test = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(s.validPalindrome(test))


