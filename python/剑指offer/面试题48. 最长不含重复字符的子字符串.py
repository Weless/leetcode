class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,tmp = 0,0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i-=1
            tmp = tmp + 1 if j - i > tmp else j - i
            res = max(tmp,res)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        tail = 0
        if len(s) < 2: return len(s)  # 边界条件
        res = 1

        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head: tail]:
                res = max(tail - head + 1, res)
            else:
                while s[tail] in s[head: tail]:
                    head += 1
        return res

# 优化
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, head = {}, 0, -1
        for tail in range(len(s)):
            if s[tail] in dic:
                head = max(dic[s[tail]], head) # 更新左指针 i
            dic[s[tail]] = tail # 哈希表记录
            res = max(res, tail - head) # 更新结果
        return res


s = Solution()
test = "dvdf"
print(s.lengthOfLongestSubstring(test))