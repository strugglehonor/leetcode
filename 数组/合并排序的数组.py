class Solution:
    """
    A, B 为两个排序数组
    """
    def merge(self, A, m: int, B, n: int):
        """
        Do not return anything, modify A in-place instead.
        """
        # 这个题其实不难，只是要考虑一些特殊情况，以及and和or这些条件想清楚
        p = m+n-1
        pA = m-1
        pB = n-1
        while pA>=0 and pB>=0:
            if A[pA] > B[pB]:
                A[p] = A[pA]
                p -= 1
                pA-=1
            else:
                A[p] = A[pB]
                p -= 1
                pB-=1
