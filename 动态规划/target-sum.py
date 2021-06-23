# https://leetcode-cn.com/problems/target-sum/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 设nums和为s，
        # 由方程 
        if (sum(nums)+target)%2 != 0 or sum(nums) < target:
            return 0
        neg = (sum(nums)+target)//2
        # 问题转化为找neg的值
        dp = [0]*(neg+1)
        dp[0] = 1
        for num in nums:
            i = neg
            while i >= 0 and i >= num:
                dp[i] += dp[i-num]
                i -= 1
        return dp[neg]
