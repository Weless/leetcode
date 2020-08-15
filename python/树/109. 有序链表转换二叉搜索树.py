class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def helper(nums):
            left,right = 0,len(nums)-1
            if left > right: return
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid+1])
            return root
        return helper(nums)
