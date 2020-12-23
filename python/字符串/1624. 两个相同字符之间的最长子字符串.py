class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        from collections import defaultdict
        d = defaultdict(list)
        for i,v in enumerate(s):
            d[v].append(i)

        ans = -1
        for _,alist in d.items():
            if len(alist) >1:
                a,b = alist[0],alist[-1]
                ans = max(ans,b-a-1)
        return ans

s = Solution()
test = "cabbac"
print(s.maxLengthBetweenEqualCharacters(test))