# -*- coding:utf-8 -*-
class Solution:
    # 这是《剑指offer》一样的解法，但是力扣上只打败了很少人
    def fib(self, n):
        a = [0,1]
        if n < 2:
            return a[n]
        fibA = 0
        fibB = 1
        for i in range(2, n+1):
            F = fibA + fibB
            fibA = fibB
            fibB = F
        return F