class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=l=r=0
        while r<len(s):
            if s[r]in s[l:r]:l+=1
            else:r+=1;length=max(length,r-l)
        return length

s = Solution()
test = "abcabcbb"
print(s.lengthOfLongestSubstring(test))