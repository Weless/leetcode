from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i,_ in enumerate(arr):
            j = i + 1
            if i == len(arr)-1:
                continue
            else:
                arr[i] = max(arr[j:])

        arr[-1] = -1
        return arr

s = Solution()
arr = [17,18,5,4,6,1]
print(s.replaceElements(arr))

class Solution2:

    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * (n-1) + [-1]
        for i in range(n-2, -1, -1):
            print(arr[i+1])
            ans[i] = max(ans[i+1], arr[i+1]) # 因为ans[i+1]已经是刚刚计算出来最大的数，因此，只要比arr[i+1]和ans[i+1]哪一个大，就作为ans[i]的值

        return ans

s2 = Solution2()
print(s2.replaceElements(arr))