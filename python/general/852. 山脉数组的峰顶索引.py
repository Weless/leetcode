class Solution:
    def peakIndexInMountainArray(self, A):
        maxNum, maxIndex = A[0],0
        i = 1
        while i < len(A)-1:
            if A[i] > maxNum:
                maxIndex = i
                maxNum = A[i]
            i+=1
        return maxIndex

class Solution2:
    def peakIndexInMountainArray(self, A):
        return A.index(max(A))

class Solution3:
    def peakIndexInMountainArray(self, A):
        return sorted(enumerate(A),key=lambda x: x[1],reverse=True)[0][0]



s = Solution3()
print(s.peakIndexInMountainArray(A =[0,2,1,0]))



### other answer
# binary search
'''
    def peakIndexInMountainArray(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) / 2
            if A[m] < A[m + 1]:
                l = m + 1
            else:
                r = m
        return l

'''