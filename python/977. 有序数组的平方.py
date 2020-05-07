class Solution:
    def sortedSquares(self, A):
        return sorted(map(lambda x:x**2,A))


class Solution2:
    def sortedSquares(self, A):
        return list(map(lambda x: x**2,sorted(A,key=lambda x:abs(x))))

import collections
class Solution3:
    def sortedSquares(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)



s = Solution3()
print(s.sortedSquares([-7,-3,2,3,11]))


### other answer

''' 不用dequeue
def sortedSquares(self, A):
	answer = [0] * len(A)
	l, r = 0, len(A) - 1
	while l <= r:
		left, right = abs(A[l]), abs(A[r])
		if left > right:
			answer[r - l] = left * left
			l += 1
		else:
			answer[r - l] = right * right
			r -= 1
	return answer
'''
