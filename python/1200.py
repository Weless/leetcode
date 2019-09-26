class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        result = []
        minList = []
        if len(arr) == 2:
            return [arr]
        for i in range(1,len(arr)):
            minList.append(arr[i]-arr[i-1])
        minNum = min(minList)
        for num in range(len(minList)):
            if minList[num] == minNum:
                result.append([arr[num],arr[num+1]])
        return result

s = Solution()
print(s.minimumAbsDifference(arr=[3,8,-10,23,19,-4,-14,27]))

### other answer

'''

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]     
        
'''