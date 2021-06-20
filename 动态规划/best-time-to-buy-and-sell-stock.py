class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: 
            return 0
        maxval = 0
        for i in range(1, len(prices)):
            if (prices[i] - min(prices[:i])) > maxval:
                maxval = prices[i] - min(prices[:i])
        return maxval
