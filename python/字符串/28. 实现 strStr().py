class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        for i in range(len(haystack)):
            j = i+len(needle)
            if j<=len(haystack):
                if haystack[i:j] == needle:
                    return i
        return -1
s = Solution()
haystack = "hello"
needle = "ll"
print(s.strStr(haystack,needle))