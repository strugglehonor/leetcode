class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 包括0，f(amount)一共amount+1个元素
        dp = [float('inf')]*(amount+1)
        # 初始值dp[0]=0
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
