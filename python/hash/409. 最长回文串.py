class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        res = 0
        ok = False
        for v in d.values():
            if v % 2 == 0 :
                res += v
            else:
                res += v-1
                ok = True
        if ok: res += 1
        return res
s = Solution()
test = "aaa"
print(s.longestPalindrome(test))