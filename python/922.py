class Solution:
    def sortArrayByParityII(self,A):
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        result = []
        for index in range(len(A)):
            if index % 2 == 0:
                result.append(even.pop())
            else:
                result.append(odd.pop())
        return result


s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))


### better answer

'''
class Solution:
    def sortArrayByParityII(self, a):
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a
'''