class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for i in S:
            if i in J:
                num += 1
        return num

    def numJewelsInStones2(self, J: str, S: str) -> int:
        result = list(map(S.count,J))
        return sum(map(J.count, S))



s = Solution()
print(s.numJewelsInStones2("aA","aAAbbbb"));


#### other method
'''
def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))
def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))               # this one after seeing https://discuss.leetcode.com/post/244105
def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
'''