# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # 和斐波那契数列一样
        a, b = 0,1
        for i in range(n+1):
            a, b = b, a+b
        return a
