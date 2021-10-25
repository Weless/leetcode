from typing import List
# 暴力
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        _max = float('-inf')
        for i in range(len(nums1)):
            j = i
            while j < len(nums2):
                if nums2[j] >= nums1[i]:
                    _max = max(_max,j-i)
                j+=1
        return 0 if _max == float('-inf') else _max



# 二分
# 思路，针对每一个nums1中的元素，对nums2进行二分查找，查找最右边的位置
# 通过, 效率不高
class Solution2:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        _max = 0
        for i in range(len(nums1)):
            t = self.bsSearch(nums2,nums1[i])
            if t == 0:
                continue
            print(i, t)
            _max = max(_max,t-i)
        return _max

    def bsSearch(self,nums,target):
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                l = mid+1
            else:
                r = mid
        if nums[l] >= target:
            return l
        else:
            return l - 1

# 双指针
class Solution3:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        _max = 0
        for i in range(len(nums1)):
            t = self.bsSearch(nums2,nums1[i])
            if t < i:
                continue
            print(i,t)
            _max = max(_max,t-i)
        return _max

    def bsSearch(self,nums,target):
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                l = mid
            else:
                r = mid-1
        return r


s = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
# print(s.maxDistance(nums1,nums2))



s3 = Solution3()
nums3 = [2,2,2]
nums4 = [10,10,1]
print(s3.bsSearch(nums4,2))
# print(s2.maxDistance(nums1,nums2))
