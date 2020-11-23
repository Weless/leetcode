class Solution:
    def sortArrayByParity(self, A):
        even = []
        odd = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd

class Solution2:
    def sortArrayByParity(self, A):
        result = []
        for i in A:
            if i % 2 == 0:
                result.insert(0,i)
            else:
                result.append(i)
        return result

class Solution3:
    def sortArrayByParity(self,A):
        i = 0
        j = len(A)-1
        while i<j:
            while A[i]%2 == 0 and i<len(A)-1:
                i+=1
            while A[j]%2 == 1 and j>0:
                if i>=j:
                    return A
                j-=1
            if i>=j:
                return A
            A[i],A[j] = A[j],A[i]
            i+=1
            j-=1
        return A

s = Solution3()
print(s.sortArrayByParity([1,0,2,4]))

#### other answer

'''
Answer1:
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        size = len(A)
        res = [None] * size
        start = 0
        end = size - 1
        for val in A:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res
        
Answer2:
return sorted(A, key=lambda x: x % 2)
'''