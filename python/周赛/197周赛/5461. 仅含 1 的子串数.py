class Solution:
    def numSub(self, s: str) -> int:
        nums = [i for i in s.split('0') if i != '']
        if nums == []:
            return 0
        nums = list(map(lambda x:x.count('1'),nums))
        max_target = max(nums)
        count = 0
        for i in range(1,max_target+1):
            for j in nums:
                if j-i+1 < 0:
                    continue
                count += (j-i+1)
        return count % (10**9 + 7)


s = Solution()
test = "1111111111011010011"
print(s.numSub(test))