from typing import List
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def binarySearch(nums,i,j):
            if self.res != -1: return
            if i <= j :
                mid = (i+j)//2
                if nums[mid] == mid :
                    self.res = mid
                    binarySearch(nums,i,mid-1)
                else:
                    # 先扫描左边，如果左边不存在结果再扫描右边
                    binarySearch(nums,i,mid-1)
                    if self.res == -1:
                        binarySearch(nums,mid+1,j)
        self.res = -1
        binarySearch(nums,0,len(nums)-1)
        return self.res

