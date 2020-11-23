from typing import List

# 时间复杂度O(n)，空间复杂度O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # L 和 R 分别表示左右两侧的乘积列表
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] 为索引 i 左侧所有元素的乘积
        # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] 为索引 i 右侧所有元素的乘积
        # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer

# 优化：空间复杂度O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Length = len(nums)
        answer = [0] * Length

        answer[0] = 1
        for i in range(1,Length):
            answer[i] = answer[i-1]*nums[i-1]

        R = 1
        for i in reversed(range(Length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer