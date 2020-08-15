class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False

        # dp存储操作数为i时的玩家的获胜情况
        dp = [False] * (N+1)
        dp[1] = False
        dp[2] = True

        for i in range(3,N+1):
            for x in range(1,i):
                # 玩家都以最佳状态，即玩家操作i后的操作数i - x应尽可能使对手输，即dp[i - x]应尽可能为false
                # 所以遍历x = 1~i-1, 寻找x的约数，使得dp[i - x] = false
                # 那么dp[i] = true即当前操作数为i的玩家能获胜
                # 如果找不到则为false，会输掉

                if i%x == 0 and not dp[i-x]:
                    dp[i] =True
                    break
        return dp[N]