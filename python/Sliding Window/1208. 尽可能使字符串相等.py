class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        totol_cost = 0
        left,right=0,0
        while right < len(s):
            totol_cost += abs(ord(s[right])-ord(t[right]))
            if totol_cost > maxCost:
                totol_cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            right+=1
        return right - left

S = Solution()
s = "abcd"
t = "bcdf"
maxCost = 3
print(S.equalSubstring(s,t,maxCost))