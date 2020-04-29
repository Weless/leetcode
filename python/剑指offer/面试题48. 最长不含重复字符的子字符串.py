class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i,j = 0, 1
        res = set()
        res.add(s[i])
        maxNum = 0
        count = 1
        while i < len(s) and j < len(s):
            if s[j] not in res:
                res.add(s[j])
                count+=1
                j+=1
            else:
                i+=1
                j=i+1
                maxNum = max(count, maxNum)
                count = 1
                res.clear()
                res.add(s[i])
        maxNum = max(count,maxNum)
        return maxNum

s = Solution()
test = "dvdf"
print(s.lengthOfLongestSubstring(test))