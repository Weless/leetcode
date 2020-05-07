class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):
            tmp = 0
            while n:
                n, b = divmod(n, 10)
                tmp += b ** 2
            return tmp

        slow = n
        fast = helper(n)
        while fast != 1 and slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        return fast ==1