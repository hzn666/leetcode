from heapq import *


class MedianFinder:
    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半

    def addNum(self, num):
        if len(self.A) == len(self.B):
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
        else:
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))

    def findMedian(self):
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.
