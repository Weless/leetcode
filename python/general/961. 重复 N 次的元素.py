import collections
class Solution:
    def repeatedNTimes(self, A):
        return collections.Counter(A).most_common(1)[0][0]

s = Solution()
print(s.repeatedNTimes([5,1,5,2,5,3,5,4]))



### other solution
'''
def repeatedNTimes(self, A):
    while 1:
        s = random.sample(A, 2)
        if s[0] == s[1]:
            return s[0]
            
class Solution:
	def repeatedNTimes(self, A: List[int]) -> int:
		B = set(A)
		return (sum(A) - sum(B)) // (len(A) - len(B))
		
		
		
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """
        :type :A List[int]
        :rtype int
        """
        d = {}
        for num in A:
            if num in d.keys():
                return num
            else:
                d[num] = 1
'''