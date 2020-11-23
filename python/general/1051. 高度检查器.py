# 先排序，后比较
class Solution:
    def heightChecker(self, heights):
        tmp = sorted(heights)
        i = 0
        count = 0
        while i < len(heights):
            if tmp[i] != heights[i]:
                count+=1
            i+=1
        return count

# 计数排序
class Solution:
    def heightChecker(self, heights):
        arr = [0 for _ in range(len(heights)+1)]
        for i in heights:
            arr[i]+=1
        count = 0
        i,j = 1,0
        while i<len(arr):
            while arr[i]>0:
                arr[i]-=1
                if heights[j] != i:
                    count +=1
                j+=1
            i+=1
        return count
