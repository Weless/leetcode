class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def permutation(nums):
            i = len(nums) - 1
            while i>0 and nums[i-1]>=nums[i]:
                i-=1
            if i<=0:
                return False

            j = len(nums) -1
            while nums[i-1] >= nums[j]:
                j-=1

            nums[i-1],nums[j] = nums[j],nums[i-1]

            nums[i:] = nums[len(nums)-1:i-1:-1]
            return True

        nums = list(range(1,n+1))
        if k == 1:
            return "".join([str(i) for i in nums])
        index = 2
        while True:
            permutation(nums)
            # print(nums)
            if k == index:
                return "".join([str(i) for i in nums])
            index+=1
s = Solution()
n = 3
k = 1
print(s.getPermutation(n,k))