from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, end, mid)

        # 合并两个有序数组
        def merge(nums, start, end, mid):
            i,j,tmp = start,mid+1,[]
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i+=1
                else:
                    self.cnt += mid - i + 1
                    tmp.append(nums[j])
                    j+=1
            while i <= mid:
                tmp.append(nums[i])
                i+=1
            while j <= end:
                tmp.append(nums[j])
                j+=1
            for i in range(len(tmp)):
                nums[start+i] = tmp[i]
        self.cnt = 0
        mergeSort(nums,0,len(nums)-1)
        return self.cnt

s = Solution()
nums = [7,5,6,4]
print(s.reversePairs(nums))