# 中心扩展法
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                self.res += 1
        for i in range(n):
            helper(i,i) # 奇数子串
            helper(i,i+1) # 偶数子串
        return self.res

s = Solution()
test = "aaaa"
print(s.countSubstrings(test))