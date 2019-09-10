class Solution:
    def flipAndInvertImage(self, A):
        result = []
        for i in A:
            tmp = []
            for j in reversed(i):
                if j == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            result.append(tmp)
        return result


s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))


### other answer

'''
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return [[1-i for i in row[::-1]] for row in A]
'''