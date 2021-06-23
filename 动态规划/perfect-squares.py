#https://leetcode-cn.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [x*x for x in range(int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for num in nums:
            for i in range(num, n+1):
                dp[i] = min(dp[i], dp[i-num]+1)
        return dp[n]
