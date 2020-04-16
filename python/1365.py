class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result= []
        for id in range(len(nums)):
            count = 0
            for num in nums:
                if num < nums[id]:
                    count +=1
            result.append(count)
        return result

s = Solution()
input = [8,1,2,2,3]
print(s.smallerNumbersThanCurrent(input))


# better answer

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         new = sorted(nums)
#         L = []
#         for num in nums:
#             L.append(new.index(num))
#         return L

