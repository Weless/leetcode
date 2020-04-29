class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        import sys
        i=0
        _max =  -1 * sys.maxsize
        while i<len(s)-1:
            left = s[:i+1]
            right = s[i+1:]
            # print(left,right)
            _max = max(left.count('0') + right.count('1'),_max)
            i+=1
        return _max

s = Solution()
test = "1111"
print(s.maxScore(test))