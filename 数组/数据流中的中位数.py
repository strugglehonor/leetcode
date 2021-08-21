from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = [] # 小顶堆
        self.B = [] # 大顶堆

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
        else:
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))


    def findMedian(self) -> float:
        return self.A[0] if len(self.A)!=len(self.B) else (self.A[0]-self.B[0])/2.0
