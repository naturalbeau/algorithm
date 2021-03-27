#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, len(coins) + 1):
            dp[0] = 1
            for j in range(1, amount+1):
                
                if j >= coins[i-1]:
                    dp[j] += dp[j-coins[i-1]]
        return dp[-1]

# @lc code=end

# 1 DP O(M*K) O(M*K)
    # def change(self, amount: int, coins: List[int]) -> int:
    #     dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
    #     dp[0][0] = 1
    #     for i in range(1, len(coins) + 1):
    #         dp[i][0] = 1
    #         for j in range(1, amount+1):
    #             dp[i][j] = dp[i-1][j]
    #             if j >= coins[i-1]:
    #                 dp[i][j] += dp[i][j-coins[i-1]]
    #     return dp[-1][-1]
# 2 DP O(M*K) O(M)