# https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-huan-s-xopj/
# 剪绳子 https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
def cuttingRope(n):
    if n < 2:
        return 0
    if n < 4:
        return n-1
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    res = res*n
    return res